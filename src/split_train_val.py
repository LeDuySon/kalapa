import pandas as pd
import numpy as np
from utils import FeatureFromColumn
from sklearn import preprocessing

def spanOneHot2dict(col):
    cols = []
    vc = col.value_counts()
    spaned = pd.get_dummies(col, prefix_sep='_', drop_first=(len(vc) < 3))
    for k in spaned.columns:
        cols.append(spaned[k].rename('%s_%s' % (col.name, k)))
    return cols

def new_column(data0, f, newname, onehot=False):
    col = data0[f.colname].rename(newname)
    for repl in f.repls:
        if isinstance(repl, dict):
            col.replace(repl, inplace=True)
        elif callable(repl):
            col = col.apply(repl)
    # transform
    if f.groups:
        if isinstance(f.groups, dict) and len(f.groups) > 0:
            def tt(x):
                for name, g_range in f.groups.items():
                    if isinstance(g_range, tuple):
                        if (x >= g_range[0]) and (x <= g_range[1]):
                            return name
                    elif isinstance(g_range, list):
                        if x in g_range:
                            return name
                    elif callable(g_range):
                        if g_range(x):
                            return name
                return x
            col = col.apply(tt)
    # Normalize
    if f.isCat:
        if onehot:
            cols = spanOneHot2dict(col)
            return cols
        else:
            #le = preprocessing.LabelEncoder()
            #col = pd.Series(le.fit_transform(col), index=data0.index, name=col.name)
            col = pd.Series(col, index=data0.index, name=col.name)
    else:
        if f.fix_range:
            m0 = col.min()
            m1 = col.max()
            col = col.apply(lambda x:(x - m0)/(m1 - m0)*2 - 1)
        else:
            m = col.mean()
            std = col.std()
            col = col.apply(lambda x:((x-m)/std) )
    return [col]



def calcWeight(col):
    a = col.value_counts()
    n = len(col)/len(a)
    b = (n/a).rename('weight')
    c = pd.merge(col, b, how='left', left_on='label', right_index=True)
    return c['weight']


def features2Dataset(data, lblname, features_desc, allSingleForNN=False):
    cols = []
    for i, f in enumerate(features_desc):
        newname = '%d_%s' % (i, f.colname)
        print(newname)
        newcols = new_column(data, f, newname, onehot=allSingleForNN)
        cols += newcols 
    if lblname and len(lblname) > 0:
        cols.append(data[lblname])
    return pd.DataFrame({col.name:col for col in cols})


from sklearn.utils import shuffle

def overSampling(data, label, ratio_total_after=1.0):
    vc = data[label].value_counts()
    target_n = vc.max()
    target_n = int(ratio_total_after * target_n)
    oversampled = []
    for lbl, count in vc.items():
        subset = data[data[label] == lbl]
        repeated_m = target_n//len(subset)
        oversampled += [subset]*repeated_m
        mod_m = target_n%len(subset)
        oversampled.append(subset.sample(mod_m, replace=False))
    oversampled = pd.concat(oversampled, axis=0)
    oversampled = shuffle(oversampled)
    oversampled.index = list(range(len(oversampled)))
    return oversampled


from sklearn.model_selection import StratifiedKFold

def dataset2Folds(data, label, kfold=10, seed=None): # leave one out ?
    skf = StratifiedKFold(n_splits=kfold, random_state=seed, shuffle=True)
    other_columns = [c for c in data.columns if c != label]
    folds = skf.split(data[other_columns], data[label])
    return list(folds)


from matplotlib import pyplot as plt
from sklearn.metrics import roc_curve, auc

def auc_plot(ytrue, ypredicted, pos_label=1):
    fpr, tpr, _ = roc_curve(ytrue, ypredicted, pos_label=pos_label)
    roc_auc = auc(fpr, tpr)
    print('ROC: %f' % roc_auc)
    gini_score = 2*roc_auc - 1
    print('Gini: %f' % gini_score)
    plt.figure()
    lw = 2
    plt.plot(fpr, tpr, color='darkorange',
             lw=lw, label='ROC curve (area = %0.2f)' % roc_auc)
    plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver operating characteristic example')
    plt.legend(loc="lower right")
    plt.show()

def auc_value(ytrue, ypredicted, pos_label=1):
    fpr, tpr, _ = roc_curve(ytrue, ypredicted, pos_label=pos_label)
    roc_auc = auc(fpr, tpr)
    gini_score = 2*roc_auc - 1
    return gini_score


# class MyModel(object):
    
#     def __init__(self, params):
#         self.reinit(params)
        
#     def reinit(self, params):
#         self.params = params
#         pass

#     def balance_train(self, train_ds):
#         pass
    
#     def predict_proba(self, Xp):
#         predicted_label = model.predict_proba(Xp)
#         return predicted_label
    
#     def kfold_init_train_eval(self, data, kfold=10, seed=8, params={}):
#         folds = dataset2Folds(data, 'label', kfold=kfold, seed=self.params['seed'])
#         predicted_labels = []
#         for i in range(len(folds)):
#             print('.', end='')
#             train_idx, test_idx = folds[i]
#             # re-init
#             self.reinit(params)
#             # balance_train       
#             train_ds = data.iloc[train_idx]
#             self.balance_train(train_ds, 'label')
#             # predict
#             test_ds = data.iloc[test_idx]
#             other_columns = [c for c in data.columns if c != 'label']
#             predicted_label = self.model.predict_proba(test_data[other_columns])
#             # agg predictions
#             predicted_labels.append(pd.DataFrame(index=test_ds.index, data=predicted_label, columns=[0,1]))


#         predicted = pd.concat(predicted_labels).sort_index()
#         return auc_value(data['label'], predicted[1])



# import time
# def ttt(model, data, fixed, varied, ret, kfold):
#     if len(varied) > 0:
#         k = next(iter(varied))
#         lspace = varied.pop(k)
#         for v in lspace:
#             if v.is_integer():
#                 v = int(v)
#             newfixed = fixed.copy()
#             newfixed[k] = v
#             ttt(newfixed, varied.copy(), ret, kfold)
#     else:
#         vs = []
#         millis = int(round(time.time() * 1000))%100000
#         print(millis)
#         for seed in range(millis, millis + 4):
#             v = model.kfold_init_train_eval(data, kfold=kfold, seed=seed, fixed)
#             vs.append(v)
#         vs = np.array(vs)
#         fixed.update({'mean':vs.mean()*100, 'std':vs.std()*100})
#         print()
#         print(fixed)
#         ret.append(fixed)
        
# def modelScanOptimizedParams(model, params_range, data):
#     ret = []
#     ttt(model, data, {} , params_range, ret, kfold=10) 
#     return ret