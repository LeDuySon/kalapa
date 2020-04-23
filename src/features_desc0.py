from utils import FeatureFromColumn
import numpy as np


########## NULL MAIN DATASET
main_null_list = []

current_col = 'FIELD_7'
f = FeatureFromColumn(current_col, 'label')
f.excls = []
f.repls = [{np.nan:''}]
f.groups = {'LNone':lambda x: len(x.strip())==0, \
            'Empty':lambda x: len(x.strip())==2, \
            'Not-Empty':lambda x: len(x.strip())>2}
f.isSure = True
main_null_list.append(f)
current_col = 'FIELD_5'
f = FeatureFromColumn(current_col, 'label')
f.excls = []
f.repls = []
f.groups = {'LNone':lambda x: x != x, 'A':(-1,0.5), 'B':(0.5,15)}
f.confStr = 'maybe_true'
f.isSure = True # plausible
main_null_list.append(f)
current_col = 'age_source1'
f = FeatureFromColumn(current_col, 'label')
f.excls = []
f.repls = [{np.nan:-1}]
f.groups = {}
f.isCat = False
f.fix_range = False
f.isSure = True 
main_null_list.append(f)
current_col = 'age_source1'
f = FeatureFromColumn(current_col, 'label')
f.excls = []
f.repls = [{np.nan:-1}]
f.groups = {'LNone':lambda x: x < 0, \
            'Young':lambda x: (x < 30) & (x>= 0), \
            'Old':lambda x: (x>=30)}
f.isSure = True 
main_null_list.append(f) 
current_col = 'FIELD_48'
f = FeatureFromColumn(current_col, 'label')
f.excls = []
f.repls = []
f.groups = {}
f.confStr = 'maybe_true'
f.isSure = True # plausible
main_null_list.append(f)
current_col = 'FIELD_4'
f = FeatureFromColumn(current_col, 'label')
f.excls = []
f.repls = []
f.groups = {'LNone':lambda x: x != x, 'A':(-1,0.5), 'B':(0.5,15)}
f.isSure = False
main_null_list.append(f)
current_col = 'FIELD_2'
f = FeatureFromColumn(current_col, 'label')
f.excls = []
f.repls = []
f.groups = {}
f.isSure = False
main_null_list.append(f)
current_col = 'FIELD_1'
f = FeatureFromColumn(current_col, 'label')
f.excls = []
f.repls = []
f.groups = {}
f.isSure = False
main_null_list.append(f)


########## NULL Fprovince
Fprovince_null_list = []
current_col = 'vung'
f = FeatureFromColumn(current_col, 'label')
f.excls = []
f.repls = []
f.groups = {}
f.isSure = True
current_col = 'mien'
f = FeatureFromColumn(current_col, 'label')
f.excls = [{np.nan:'LNONE'}]
f.repls = []
f.groups = {}
f.isSure = True



#### NULL F7ext
F7ext_null_list = []
current_col = 'CH'
f = FeatureFromColumn(current_col, 'label')
f.excls = []
f.repls = []
f.groups = {}
f.confStr = 'maybe_true'
f.isSure = True #plausible
F7ext_null_list.append(f)
current_col = 'f7count'
f = FeatureFromColumn(current_col, 'label')
f.excls = []
f.repls = []
f.groups = {}
f.isCat = False
f.confStr = 'maybe_true'
f.isSure = True #plausible
F7ext_null_list.append(f)


null_list = main_null_list + Fprovince_null_list + F7ext_null_list