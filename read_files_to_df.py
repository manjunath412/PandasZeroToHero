import os
import pandas as pd

def read_files(input_dir):
    # Read the CSV files into DataFrames
    fam_df = pd.read_csv(os.path.join(input_dir, 'fam.csv'))
    id_id_df = pd.read_csv(os.path.join(input_dir, 'id_id.csv'), delimiter='\t')
    ad_df = pd.read_csv(os.path.join(input_dir, 'ad.csv'))
    ad_id_df = pd.read_csv(os.path.join(input_dir, 'ad_id.csv'), delimiter='\t')
    ad_bd_df = pd.read_csv(os.path.join(input_dir, 'ad_bd.csv'), delimiter='\t')
    ch_df = pd.read_csv(os.path.join(input_dir, 'ch.csv'))
    ch_id_df = pd.read_csv(os.path.join(input_dir, 'ch_id.csv'), delimiter='\t')
    ch_bd_df = pd.read_csv(os.path.join(input_dir, 'ch_bd.csv'), delimiter='\t')
    
    return fam_df, id_id_df, ad_df, ad_id_df, ad_bd_df, ch_df, ch_id_df, ch_bd_df

input_dir = '/in-folder'

fam_df, id_id_df, ad_df, ad_id_df, ad_bd_df, ch_df, ch_id_df, ch_bd_df = read_files(input_dir)
