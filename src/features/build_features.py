import pandas as pd

def map_icd9(code):
    if pd.isna(code):
        return 'Unknown'
    c = str(code).strip()
    if c.startswith('V'): return 'Supplementary'
    if c.startswith('E'): return 'External'
    try:
        num = float(c)
    except:
        return 'Unknown'
        
    if 1 <= num <= 139: return 'Infectious'
    elif 140 <= num <= 239: return 'Neoplasms'
    elif 240 <= num <= 279: return 'Endocrine'
    elif 390 <= num <= 459: return 'Circulatory'
    elif 460 <= num <= 519: return 'Respiratory'
    else: return 'Other'

def make_features(df):
    # binary target
    df['target'] = (df['readmitted'] == '<30').astype(int)
    df = df.drop(columns=['readmitted'])
    
    # prior visits
    df['total_prior_visits'] = df['number_inpatient'] + df['number_emergency'] + df['number_outpatient']
    
    # diabetes meds
    meds = ['metformin', 'repaglinide', 'nateglinide', 'chlorpropamide', 'glimepiride', 'glipizide', 'glyburide', 'pioglitazone', 'rosiglitazone', 'acarbose', 'insulin']
    # only count ones that are in df
    meds = [m for m in meds if m in df.columns]
    df['n_diabetes_meds'] = (df[meds].fillna('No') != 'No').sum(axis=1)
    
    # icd9 groups
    for col in ['diag_1', 'diag_2', 'diag_3']:
        df[col + '_group'] = df[col].apply(map_icd9)
    df = df.drop(columns=['diag_1', 'diag_2', 'diag_3'])
    
    return df
