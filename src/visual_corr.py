import numpy as np 
import pandas as pd
from matplotlib import pyplot as plt
from scipy.stats import iqr
import math
from matplotlib.lines import Line2D
unfilled_markers = [m for m, func in (Line2D.markers.items())
                    if func != 'nothing' and m not in Line2D.filled_markers]

def autolabel(rects, axe, labels):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for i, rect in enumerate(rects):
        height = rect.get_height()
        axe.annotate('{}'.format(labels[i]),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom',
                    rotation=90)
        
def drawRow(axe, data, name):
    data.fillna(0, inplace=True)
    data_normalized = data/data.sum()
    n = len(data.columns) 
    width = 0.7/n
    for i, col in enumerate(data.columns):
        x = np.arange(len(data[col]))
        #print(x + (i - (n-1)/2)*width)
        #print(data_normalized[col])
        rects1 = axe.bar(x + (i - (n-1)/2)*width, data_normalized[col], width, label=col)
        autolabel(rects1, axe, data[col].values)
    axe.set_ylim(0,data_normalized[col].max()*1.5)
    axe.set_ylabel(name)
    axe.set_xticks(x)
    axe.set_xticklabels(data.index, rotation='vertical')
    axe.legend()


def calcBinWidth(array):
    IQR = iqr(array)
    n = len(array)
    return 2*IQR*math.pow(n,-0.3333)

def calcBinCount(array):
    width = calcBinWidth(array)
    return int((array.max() - array.min())/calcBinWidth(array)) + 1

def cat_cat(data, cat1, cat2, label, draw_to = '../temp/test.png', figsize=(6,4)):
    t = data.groupby([cat1, cat2, label]).size()
    # if len(t.index.levels[0]) > len(t.index.levels[1]):
    #     t = t.swaplevel(0, 1)
    t = t.unstack(level=1).fillna(0).stack().swaplevel(1,2)
    n = len(t.index.levels[0])
    plt.cla()
    plt.clf()
    fig = plt.figure(figsize=figsize)
    axes = []
    for i, lv in enumerate(t.index.levels[0]):
        data = t.loc[lv].unstack()
        if i == 0:
            ax = fig.add_subplot(n,1,i+1)
        else:
            ax = fig.add_subplot(n,1,i+1, sharex=axes[0])
        drawRow(ax, data, lv)
        axes.append(ax)
    ax.set_xlabel(t.index.names[1])
    plt.title(t.index.names[0], rotation='vertical',x=-0.1,y=0.5)
    fig.tight_layout()
    plt.savefig(draw_to)
    return t
    
def cont_cont(data, cont1, cont2, label, draw_to = '../temp/test.png', sample_to_balance_frequentis=True, figsize=(6,4)):
    t = data[[label, cont1, cont2]].set_index([label])
    plot_data = {}
    min_len = len(data)
    for j, lb in enumerate(data[label].unique()):
        tlabel = t.loc[lb].dropna()
        plot_data[lb] = t.loc[lb].dropna()
        min_len = min(len(tlabel), min_len)
    plt.cla()
    plt.clf()
    fig = plt.figure(figsize=figsize)
    axe = fig.add_subplot(111)
    for i, (lb, dat) in enumerate(plot_data.items()):
        if sample_to_balance_frequentis:
            dat = dat.sample(n=min_len, random_state=99)
        axe.scatter(dat[cont1].values, dat[cont2].values,label=lb, marker=unfilled_markers[i+1])
    
    axe.set_ylabel(cont2)
    axe.set_xlabel(cont1)
    axe.legend()

    plt.savefig(draw_to)
    
def cat_cont(data, cat, cont, label, draw_to = '../temp/test.png', binCount=None, figsize=(6,4)):
    t = data[[cat, label, cont]].set_index([cat, label])
    plt.cla()
    plt.clf()
    fig = plt.figure(figsize=figsize)
    n = len(t.index.levels[0])
    axes = []
    for i, lv in enumerate(t.index.levels[0]):
        if i == 0:
            ax = fig.add_subplot(n,1,i+1)
        else:
            ax = fig.add_subplot(n,1,i+1, sharex=axes[0])
        axes.append(ax)
        tcat = t.loc[lv]
        for j, lb in enumerate(t.index.levels[1]):
            tlabel = tcat.loc[lb].dropna()
            if len(tlabel) > 20:
                bc = calcBinCount(tlabel[cont]) if binCount is None else binCount
                ax.hist(tlabel[cont].values, bc, density=True,alpha=0.75, label=lb)
        ax.set_ylabel(lv)
        ax.legend()
    ax.set_xlabel(cont)
    fig.tight_layout()
    plt.title(cat, rotation='vertical',x=-0.1,y=0.5)
    plt.savefig(draw_to)


def cont_label(data, cont, label, draw_to = '../temp/test.png', binCount=None, figsize=(6,4)):
    t = data[[label, cont]].set_index([label])
    plt.cla()
    plt.clf()
    fig = plt.figure(figsize=figsize)
    axe = fig.add_subplot(111)
    for j, lb in enumerate(data[label].unique()):
        tlabel = t.loc[lb].dropna()
        if len(tlabel) > 20:
            bc = calcBinCount(tlabel[cont]) if binCount is None else binCount
            axe.hist(tlabel[cont].values, bc, density=True,alpha=0.75, label=lb)
    axe.set_xlabel(cont)
    plt.savefig(draw_to)
    
def cat_label(data, cat, label, draw_to = '../temp/test.png', figsize=(6,4), sort_count=False):
    t = data.groupby([cat, label]).size()
    data = t.unstack().fillna(0)
    plt.cla()
    plt.clf()
    fig = plt.figure(figsize=figsize)
    axe = fig.add_subplot(111)
    if sort_count:
        data['sum'] = data.sum(axis=1)
        data.sort_values('sum', inplace=True)
        del data['sum']
    drawRow(axe, data, cat)
    axe.set_xlabel(cat)
    plt.savefig(draw_to)
    return data

def type2func1(f1_type, f1):
    if f1_type == 'cat':
        return cat_label, {'cat':f1}
    elif f1_type == 'cont':
        return cont_label, {'cont':f1}
    
def type2func2(type1, f1, type2, f2):
    if (type1 == 'cat') and (type2 == 'cat'):
        return cat_cat, {'cat1':f1, 'cat2':f2}
    elif (type1 == 'cont') and (type2 == 'cont'):
        return cont_cont, {'cont1':f1, 'cont2':f2}
    elif (type1 == 'cat') and (type2 == 'cont'):
        return cat_cont, {'cat':f1, 'cont':f2}
    elif (type1 == 'cont') and (type2 == 'cat'):
        return cat_cont, {'cat':f2, 'cont':f1}

import os
#corr_with_independence_test
def corr(data, f1, f1_type, f2, f2_type, label, outdir, rawfn, num, **kwargs):

    if (f1_type is None) or (f1_type not in ['cat', 'cont']):
        if (f2_type is None) or (f2_type not in ['cat', 'cont']):
            raise ValueError
        else:
            fn, args = type2func1(f2_type, f2)
    else:
        if (f2_type is None) or (f2_type not in ['cat', 'cont']):
            fn, args = type2func1(f1_type, f1)
        else:
            fn, args = type2func2(f1_type, f1, f2_type, f2)

    args.update({'label':label})
    d = fn(data, **args, draw_to=os.path.join(outdir, rawfn + '_original.png'), **kwargs)
    if num == 0:
        return d

    #cat_cat(data, cat1, cat2, label, draw_to=os.path.join(outdir, rawfn + '_original.png'))
    a = data[label].value_counts()
    name_differences = a.index.tolist()
    prob_differences = (a/a.sum()).tolist()
    noise_data = []
    for i in range(num):
        repeated_time = np.random.multinomial(len(data), prob_differences, size=1)
        new_label = np.repeat(name_differences, repeated_time[0])
        np.random.shuffle(new_label)
        data[label + '__2'] = new_label

        args['label'] = label + '__2'
        noise0 = fn(data, **args, draw_to=os.path.join(outdir, rawfn + '_%d.png' % (i+1)), **kwargs)
        noise_data.append(noise0)
        #cat_cat(data, cat1, cat2, label + '__2', draw_to=os.path.join(outdir, rawfn + '_%d.png' % i))

    del data[label + '__2']

    return d, noise_data


def dep_test(data, f1, f2, label, draw_to):
    t = data.groupby([f1, f2, label]).size()
    t = t.unstack(level=1).fillna(0).stack().swaplevel(1,2)
    a = t.unstack().groupby(level=0).sum()
    a = a/a.sum()
    b = t.unstack().groupby(level=1).sum()
    b = b/b.sum()
    c = t.unstack()
    c = c/c.sum()
    d = c.drop(columns=c.columns)
    a = pd.merge(d, a, how='left',left_index=True, right_index=True)
    b = pd.merge(d, b, how='left',left_index=True, right_index=True)
    indjoin = (a*b)
    for cname in indjoin.columns:
        indjoin.rename(columns={cname:str(cname)+'*'}, inplace=True)
    indjoin = pd.merge(c, indjoin, how='left',left_index=True, right_index=True)
    plt.cla()
    plt.clf()
    n = len(indjoin.index.levels[0])
    m = len(indjoin.index.levels[1])
    fig, axes = plt.subplots(n,m,figsize=(2*n,2*m), sharex=True, sharey=True)
    for i, lv0 in enumerate(indjoin.index.levels[0]):
        for j, lv1 in enumerate(indjoin.index.levels[1]):
            arr = indjoin.loc[lv0, lv1]
            ax = axes[i,j]
            ax.bar(range(len(arr)), arr, 1, label=arr.index, color=['b','r','c','m'])
            ax.set_xticks(range(len(arr)))
            ax.set_xticklabels(arr.index)
            ax.set_ylim(0,1)
            if j == 0:
                ax.set_ylabel(lv0)
            if i == n - 1:
                ax.set_xlabel(lv1)
    fig.suptitle('[%s]  [%s]' % (t.index.names[0], t.index.names[1]))
    plt.savefig(draw_to)
    return indjoin


if __name__ == '__main__':
    subset = pd.read_csv('../jupyter/subset.csv')
    subset.province.replace({np.nan:'None'}, inplace=True)
    subset.age_source2.replace({-1:np.nan}, inplace=True)
    subset.FIELD_8.replace({np.nan:'None'}, inplace=True)
    # cat_cat(subset, 'FIELD_8', 'FIELD_4', 'label', draw_to = './temp/cat_cat.png')
    # cont_cont(subset, 'FIELD_5', 'age_source2', 'label', draw_to = './temp/cont_cont.png')
    # cat_cont(subset, 'FIELD_8', 'age_source2', 'label', draw_to = './temp/cat_cont.png')
    # cont_label(subset, 'age_source2', 'label', draw_to = './temp/cont_label.png')
    # cat_label(subset, 'FIELD_5', 'label', draw_to = './temp/cat_label.png')

    num=2
    # corr(subset, 'FIELD_8', 'cat', 'FIELD_4', 'cat', 'label', './temp/' , 'cat_cat' , num=num)
    # corr(subset, 'FIELD_5', 'cont', 'age_source2', 'cont', 'label', './temp/' , 'cont_cont' , num=num)
    # corr(subset, 'FIELD_8', 'cat', 'age_source2', 'cont', 'label', './temp/' , 'cat_cont' , num=num)
    # corr(subset, 'age_source2', 'cont', 'FIELD_8', 'cat', 'label', './temp/' , 'cont_cat' , num=num)
    # corr(subset, None, None, 'FIELD_5', 'cat', 'label', './temp/' , 'cat_label' , num=num)
    # corr(subset, 'age_source2', 'cont', None, None, 'label', './temp/' , 'cont_label' , num=num)
    dep_test(subset, 'FIELD_8', 'FIELD_4', 'label', './temp/test.png')