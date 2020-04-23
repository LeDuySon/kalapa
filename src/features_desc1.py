from utils import FeatureFromColumn
import numpy as np
import pandas as pd


########## MAIN DATASET
main_notnull_list = []

current_col = 'FIELD_1'
f = FeatureFromColumn(current_col, 'label')
f.excls = []
f.repls = []
f.groups = {}
f.isSure = True
main_notnull_list.append(f)
current_col = 'age_source2'
f = FeatureFromColumn(current_col, 'label')
f.excls = []
f.repls = [{np.nan:-1}]
f.groups = {}
f.confStr = 'maybe_true'
f.isCat = False
f.fix_range = True
f.isSure = True
main_notnull_list.append(f)
current_col = 'age_source1'
f = FeatureFromColumn(current_col, 'label')
f.excls = []
f.repls = [{np.nan:-1}]
f.groups = {'LNone':lambda x: x < 0, \
            'Young':lambda x: (x < 30) & (x>= 0), \
            'Old':lambda x: (x>=30)}
f.isSure = True
main_notnull_list.append(f)
current_col = 'FIELD_5'
f = FeatureFromColumn(current_col, 'label')
f.excls = []
f.repls = []
f.groups = {'A':(-1,0.5), 'B':(0.5,15)}
f.isSure = True
main_notnull_list.append(f)
current_col = 'FIELD_6'
f = FeatureFromColumn(current_col, 'label')
f.excls = []
f.repls = []
f.groups = {'A':(-1,0.5), 'B':(0.5,15)}
f.confStr = 'maybe_true'
f.isSure = True # Plausible, dont know
main_notnull_list.append(f)
current_col = 'FIELD_7'
f = FeatureFromColumn(current_col, 'label')
f.excls = []
f.repls = [{np.nan:''}]
f.groups = {'LNone':lambda x: len(x.strip())==0, \
            'Empty':lambda x: len(x.strip())==2, \
            'Not-Empty':lambda x: len(x.strip())>2}
f.isSure = True
main_notnull_list.append(f)
current_col = 'FIELD_8'
f = FeatureFromColumn(current_col, 'label')
f.excls = []
f.repls = []
f.groups = {}
f.isSure = True
main_notnull_list.append(f)
current_col = 'FIELD_10'
f = FeatureFromColumn(current_col, 'label')
f.excls = []
f.repls = []
f.groups = {}
f.confStr = 'maybe_true'
f.isSure = True # plausible
main_notnull_list.append(f)
current_col = 'FIELD_11'
f = FeatureFromColumn(current_col, 'label')
f.excls = []
f.repls = [{'None':'-1'}, pd.to_numeric]
f.groups = {'SHORT':(-2,5.5), 'LONG':(5.5,100)}
f.isSure = True 
main_notnull_list.append(f)
current_col = 'FIELD_12'
f = FeatureFromColumn(current_col, 'label')
f.excls = []
f.repls = []
f.groups = {}
f.isSure = True 
main_notnull_list.append(f)
current_col = 'FIELD_14'
f = FeatureFromColumn(current_col, 'label')
f.excls = []
f.repls = []
f.groups = {}
f.isSure = True
main_notnull_list.append(f)
current_col = 'FIELD_15'
f = FeatureFromColumn(current_col, 'label')
f.excls = []
f.repls = []
f.groups = {}
f.isSure = True
main_notnull_list.append(f)
current_col = 'FIELD_17'
f = FeatureFromColumn(current_col, 'label')
f.excls = []
f.repls = []
f.groups = {}
f.isSure = True
main_notnull_list.append(f)
current_col = 'FIELD_18'
f = FeatureFromColumn(current_col, 'label')
f.excls = []
f.repls = []
f.groups = {}
f.isSure = True
main_notnull_list.append(f)
current_col = 'FIELD_19'
f = FeatureFromColumn(current_col, 'label')
f.excls = []
f.repls = []
f.groups = {}
f.isSure = True
main_notnull_list.append(f)
current_col = 'FIELD_20'
f = FeatureFromColumn(current_col, 'label')
f.excls = []
f.repls = []
f.groups = {}
f.isSure = True
main_notnull_list.append(f)

current_col = 'FIELD_22'
f = FeatureFromColumn(current_col, 'label')
f.excls = []
f.repls = []
f.groups = {'LNone':lambda x:x!=x, 'A':(-0.5,0.5), 'B':(0.5,44.5), 'C':(44.5,100.5),'D':(100.5,1000)}
f.isSure = True
main_notnull_list.append(f)

# current_col = 'FIELD_22'
# f = FeatureFromColumn(current_col, 'label')
# f.excls = []
# f.repls = [{np.nan:'None'}, pd.to_numeric]
# f.groups = {'A':(-0.5,0.5), 'B':(0.5,44.5), 'C':(44.5,100.5),'D':(100.5,1000)}
# f.isSure = True
# main_notnull_list.append(f)

current_col = 'FIELD_25'
f = FeatureFromColumn(current_col, 'label')
f.excls = []
f.repls = []
f.groups = {}
f.isSure = True
main_notnull_list.append(f)
current_col = 'FIELD_26'
f = FeatureFromColumn(current_col, 'label')
f.excls = []
f.repls = []
f.groups = {}
f.isSure = True
main_notnull_list.append(f)
current_col = 'FIELD_29'
f = FeatureFromColumn(current_col, 'label')
f.excls = []
f.repls = []
f.groups = {}
f.isSure = True
main_notnull_list.append(f)
current_col = 'FIELD_30'
f = FeatureFromColumn(current_col, 'label')
f.excls = []
f.repls = []
f.groups = {}
f.isSure = True
main_notnull_list.append(f)
current_col = 'FIELD_31'
f = FeatureFromColumn(current_col, 'label')
f.excls = []
f.repls = []
f.groups = {}
f.isSure = True
main_notnull_list.append(f)
current_col = 'FIELD_46'
f = FeatureFromColumn(current_col, 'label')
f.excls = []
f.repls = []
f.groups = {}
f.isSure = True
main_notnull_list.append(f)
current_col = 'FIELD_47'
f = FeatureFromColumn(current_col, 'label')
f.excls = []
f.repls = []
f.groups = {}
f.confStr = 'maybe_true'
f.isSure = True #plausible
main_notnull_list.append(f)
current_col = 'FIELD_48'
f = FeatureFromColumn(current_col, 'label')
f.excls = []
f.repls = []
f.groups = {}
f.confStr = 'maybe_true'
f.isSure = True #plausible
main_notnull_list.append(f)
current_col = 'FIELD_51'
f = FeatureFromColumn(current_col, 'label')
f.excls = []
f.repls = []
f.groups = {'A':(-0.5,7.5), 'B':(7.5,44.5), 'C':(44.5,500.5)}
f.confStr = 'maybe_true'
f.isSure = True #a little plausible, is it because random in long range ?
main_notnull_list.append(f)
current_col = 'FIELD_52'
f = FeatureFromColumn(current_col, 'label')
f.excls = []
f.repls = []
f.groups = {'A':(29,32), 'B':(60,80)}
f.isSure = True 
main_notnull_list.append(f)
current_col = 'FIELD_53'
f = FeatureFromColumn(current_col, 'label')
f.excls = []
f.repls = []
f.groups = {'A':(29,32), 'B':(60,80)}
f.isSure = True 
main_notnull_list.append(f)
current_col = 'FIELD_54'
f = FeatureFromColumn(current_col, 'label')
f.excls = []
f.repls = []
f.groups = {'A':(-1,0.13),'B':(0.13,1.2)}
f.confStr = 'maybe_true'
f.isSure = True #plausible, is it because random in long range ?
main_notnull_list.append(f)
current_col = 'FIELD_56'
f = FeatureFromColumn(current_col, 'label')
f.excls = []
f.repls = []
f.groups = {'A':(-1,0.001), 'B':(0.001,1.2)}
f.isSure = True
main_notnull_list.append(f)
current_col = 'FIELD_57'
f = FeatureFromColumn(current_col, 'label')
f.excls = []
f.repls = []
f.groups = {'A':(-1,0.001), 'B':(0.001,1.2)}
f.isSure = True
main_notnull_list.append(f)
current_col = 'FIELD_2'
f = FeatureFromColumn(current_col, 'label')
f.excls = []
f.repls = []
f.groups = {}
f.isSure = False
main_notnull_list.append(f)
current_col = 'FIELD_4'
f = FeatureFromColumn(current_col, 'label')
f.excls = []
f.repls = []
f.groups = {'A':(-1,0), 'B':(1,13)}
f.isSure = False
main_notnull_list.append(f)
current_col = 'FIELD_4'
f = FeatureFromColumn(current_col, 'label')
f.excls = []
f.repls = []
f.groups = {}
f.isSure = False
main_notnull_list.append(f)
current_col = 'FIELD_9'
f = FeatureFromColumn(current_col, 'label')
f.excls = []
f.repls = []
f.groups = {'GD':['GD'], 'DN':['DN'], 'O':['79', '86', 'CC', 'MS', 'XN', '80', 'NO', 'XV', 'TC', 'TE', '75', 'TS',\
       'CB', 'HD', 'KC', 'TA', 'HX', 'HS', 'BT', 'TK', 'NN', 'HT', 'XD', 'HN',\
       'XK', 'CN', 'DT', 'SV', 'DK', 'GB', 'CH', 'HC', 'TN']}
f.isSure = False
main_notnull_list.append(f)
current_col = 'FIELD_16'
f = FeatureFromColumn(current_col, 'label')
f.excls = []
f.repls = []
f.groups = {}
f.isSure = False
main_notnull_list.append(f)
current_col = 'FIELD_33'
f = FeatureFromColumn(current_col, 'label')
f.excls = []
f.repls = []
f.groups = {}
f.isSure = False
main_notnull_list.append(f)
current_col = 'FIELD_34'
f = FeatureFromColumn(current_col, 'label')
f.excls = []
f.repls = []
f.groups = {}
f.isSure = False
main_notnull_list.append(f)
current_col = 'FIELD_35'
f = FeatureFromColumn(current_col, 'label')
f.excls = []
f.repls = []
f.groups = {}
f.isSure = False
main_notnull_list.append(f)
current_col = 'FIELD_36'
f = FeatureFromColumn(current_col, 'label')
f.excls = []
f.repls = []
f.groups = {}
f.isSure = False
main_notnull_list.append(f)
current_col = 'FIELD_37'
f = FeatureFromColumn(current_col, 'label')
f.excls = []
f.repls = [str]
f.groups = {}
f.isSure = False
main_notnull_list.append(f)
current_col = 'FIELD_39'
f = FeatureFromColumn(current_col, 'label')
f.excls = []
f.repls = []
f.groups = {'VN':['VN'], 'None':['None'], 'Rest':['VU', 'SC', 'SE', 'IT', 'IL', 'TK', 'TL', 'ES', 'DM', 'TR', 'PH', 'AU',\
       'CA', 'AE', 'DT', 'TS', 'GB', 'BE', 'N', 'DK', 'AD', 'NN', 'NL', 'FR',\
       'IN', 'NU', 'MY', 'TH', 'US', 'DE', 'KP', 'SG', 'HK', 'DL', 'UK', 'HQ',\
       '1', 'CZ', 'TQ', 'CN', 'JP', 'KR', 'TW']}
f.confStr = 'maybe_false'
f.isSure = False # plausible
main_notnull_list.append(f)
current_col = 'FIELD_40'
f = FeatureFromColumn(current_col, 'label')
f.excls = []
f.repls = []
f.groups = {}
f.confStr = 'maybe_false'
f.isSure = False # plausible
main_notnull_list.append(f)
current_col = 'FIELD_41'
f = FeatureFromColumn(current_col, 'label')
f.excls = []
f.repls = []
f.groups = {}
f.isSure = False
main_notnull_list.append(f)
current_col = 'FIELD_43'
f = FeatureFromColumn(current_col, 'label')
f.excls = []
f.repls = []
f.groups = {}
f.isSure = False
main_notnull_list.append(f)
current_col = 'FIELD_44'
f = FeatureFromColumn(current_col, 'label')
f.excls = []
f.repls = []
f.groups = {}
f.isSure = False
main_notnull_list.append(f)
current_col = 'FIELD_45'
f = FeatureFromColumn(current_col, 'label')
f.excls = []
f.repls = [str]
f.groups = {}
f.isSure = False
main_notnull_list.append(f)
current_col = 'FIELD_49'
f = FeatureFromColumn(current_col, 'label')
f.excls = []
f.repls = []
f.groups = {}
f.confStr = 'maybe_false'
f.isSure = False # plausible
main_notnull_list.append(f)
current_col = 'FIELD_50'
f = FeatureFromColumn(current_col, 'label')
f.excls = []
f.repls = []
f.groups = {'A':(29,30),'B':(55,70)}
f.isSure = False
main_notnull_list.append(f)
current_col = 'FIELD_54'
f = FeatureFromColumn(current_col, 'label')
f.excls = []
f.repls = []
f.groups = {}
f.isSure = False
main_notnull_list.append(f)


### NOT NULL Fprovince_ext = pd.read_csv('./Fprovince_ext.csv')
Fprovince_notnull_list = []
current_col = 'vung'
f = FeatureFromColumn(current_col, 'label')
f.excls = []
f.repls = [{np.nan:'LNONE'}]
f.groups = {}
f.isSure = True
Fprovince_notnull_list.append(f)


### NOT NULL F7ext = pd.read_csv('./F7ext.csv')
F7ext_notnull_list = []
current_col = 'CH'
f = FeatureFromColumn(current_col, 'label')
f.excls = []
f.repls = []
f.groups = {}
f.isCat = False
f.confStr = 'maybe_true'
f.isSure = True #plausible
F7ext_notnull_list.append(f)
current_col = 'f7count'
f = FeatureFromColumn(current_col, 'label')
f.excls = []
f.repls = []
f.groups = {}
f.isCat = False
f.confStr = 'maybe_true'
f.isSure = True #plausible
F7ext_notnull_list.append(f)


notnull_list = main_notnull_list + Fprovince_notnull_list + F7ext_notnull_list