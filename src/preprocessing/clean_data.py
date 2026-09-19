import pandas as pd
import numpy as np

def basic_cleaning(df):
    # replace ? with nan
    df = df.replace('?', np.nan)
    
    # drop death and hospice
    bad_codes = [11, 13, 14, 19, 20, 21]
    df = df[~df['discharge_disposition_id'].isin(bad_codes)].copy()
    
    # drop weight
    df = df.drop(columns=['weight'])
    
    # drop identifiers but keep patient_nbr for later maybe
    patient_ids = df['patient_nbr'].copy()
    df = df.drop(columns=['encounter_id', 'patient_nbr'])
    
    return df, patient_ids
