def filter_and_save_dataframes(fam_merged_df, ad_merged_df, ch_merged_df, output_dir):
    # Get unique reporting months from all datasets
    reporting_months = set(fam_merged_df['reporting_month'].unique())
    reporting_months.update(ad_merged_df['reporting_month'].unique())
    reporting_months.update(ch_merged_df['reporting_month'].unique())
    
    # Create a new CSV file for each reporting month
    for month in reporting_months:
        # Create a subfolder for the month within the output directory
        month_output_dir = os.path.join(output_dir, str(month))
        if not os.path.exists(month_output_dir):
            os.makedirs(month_output_dir)
        
        # Filter the merged DataFrames for the current reporting month
        fam_month_df = fam_merged_df[fam_merged_df['reporting_month'] == month]
        ad_month_df = ad_merged_df[ad_merged_df['reporting_month'] == month]
        ch_month_df = ch_merged_df[ch_merged_df['reporting_month'] == month]
        
        # Save the filtered DataFrames as CSV files in the corresponding subfolder
        fam_month_df.to_csv(os.path.join(month_output_dir, f'fam_merged_{month}.csv'), index=False)
        ad_month_df.to_csv(os.path.join(month_output_dir, f'ad_merged_{month}.csv'), index=False)
        ch_month_df.to_csv(os.path.join(month_output_dir, f'ch_merged_{month}.csv'), index=False)

    print("Processing completed successfully!")

output_dir = '/root-output-folder'
filter_and_save_dataframes(fam_merged_df, ad_merged_df, ch_merged_df, output_dir)
