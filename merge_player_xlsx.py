import os
import pandas as pd


def merge_and_find_players(file_with_info, file_with_stats, output_path):
    info_dt = pd.read_excel(file_with_info)
    stats_dt = pd.read_excel(file_with_stats)

    merged_df = pd.merge(info_dt, stats_dt, on="NAME")

    merged_df['COLLEGE'] = merged_df['COLLEGE'].replace('--', 'N/A')
    merged_df['fg_percent'] = merged_df['fg_percent'].fillna(0)
    merged_df['ft_percent'] = merged_df['ft_percent'].fillna(0)
    merged_df['fpg'] = merged_df['fpg'].fillna(0)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    merged_df.to_excel(output_path, index=False)


file1_path = 'C:/Users/jerem/OneDrive/Desktop/all_players.xlsx'
file2_path = 'C:/Users/jerem/OneDrive/Desktop/NBA_Players_stats.xlsx'
output_file_path = 'C:/Users/jerem/OneDrive/Desktop/merged_and_combined.xlsx'

merge_and_find_players(file1_path, file2_path, output_file_path)
