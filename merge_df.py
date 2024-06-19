import pandas as pd

def merge_dataframes(fam_df, id_id_df, ad_df, ad_id_df, ad_bd_df, ch_df, ch_id_df, ch_bd_df):
    # Merge the DataFrames on the 'id' column
    fam_merged_df = pd.merge(fam_df, id_id_df, on='id', how='inner')
    ad_merged_df = pd.merge(ad_df, ad_id_df, on='id', how='inner')
    ad_merged_df = pd.merge(ad_merged_df, ad_bd_df, on='id', how='inner')
    ch_merged_df = pd.merge(ch_df, ch_id_df, on='id', how='inner')
    ch_merged_df = pd.merge(ch_merged_df, ch_bd_df, on='id', how='inner')
    
    return fam_merged_df, ad_merged_df, ch_merged_df

fam_merged_df, ad_merged_df, ch_merged_df = merge_dataframes(fam_df, id_id_df, ad_df, ad_id_df, ad_bd_df, ch_df, ch_id_df, ch_bd_df)
