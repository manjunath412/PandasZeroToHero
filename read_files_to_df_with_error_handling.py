import os
import pandas as pd

def read_files(input_dir):
    try:
        # Define file paths
        fam_path = os.path.join(input_dir, 'fam.csv')
        id_id_path = os.path.join(input_dir, 'id_id.csv')
        ad_path = os.path.join(input_dir, 'ad.csv')
        ad_id_path = os.path.join(input_dir, 'ad_id.csv')
        ad_bd_path = os.path.join(input_dir, 'ad_bd.csv')
        ch_path = os.path.join(input_dir, 'ch.csv')
        ch_id_path = os.path.join(input_dir, 'ch_id.csv')
        ch_bd_path = os.path.join(input_dir, 'ch_bd.csv')

        # Read the CSV files into DataFrames
        fam_df = pd.read_csv(fam_path)
        id_id_df = pd.read_csv(id_id_path, delimiter='\t')
        ad_df = pd.read_csv(ad_path)
        ad_id_df = pd.read_csv(ad_id_path, delimiter='\t')
        ad_bd_df = pd.read_csv(ad_bd_path, delimiter='\t')
        ch_df = pd.read_csv(ch_path)
        ch_id_df = pd.read_csv(ch_id_path, delimiter='\t')
        ch_bd_df = pd.read_csv(ch_bd_path, delimiter='\t')
        
        return fam_df, id_id_df, ad_df, ad_id_df, ad_bd_df, ch_df, ch_id_df, ch_bd_df
    except FileNotFoundError as e:
        print(f"File not found: {e}")
        raise
    except pd.errors.EmptyDataError as e:
        print(f"Empty data error: {e}")
        raise
    except pd.errors.ParserError as e:
        print(f"Parsing error: {e}")
        raise
    except Exception as e:
        print(f"Error reading files: {e}")
        raise

input_dir = '/in-source-folder'

fam_df, id_id_df, ad_df, ad_id_df, ad_bd_df, ch_df, ch_id_df, ch_bd_df = read_files(input_dir)
