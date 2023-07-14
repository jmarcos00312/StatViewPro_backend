import os
import pandas as pd



def combine_excel_files(folder_path, final_file_path):

    # Getting the list of all the file names in the folder
    file_names = os.listdir(folder_path)

    # Creating an an empty DataFrame to strore the final DT
    final_data = pd.DataFrame()
    
    for file in file_names:
        file = os.path.join(folder_path, file)
        df = pd.read_excel(file)
        # Adding a new column to the DataFrame indicating the source file name
        df['team_name'] = file
        
        final_data = pd.concat([final_data, df])
        
    final_data.to_excel(final_file_path, index=False)
    
    print(f"finished! the file is at {final_file_path}")
        




folder_path = 'C:\\Users\\jerem\\OneDrive\\Desktop\\nba teams'
final_file_path ='C:\\Users\\jerem\\OneDrive\\Desktop\\all_players.xlsx'

combine_excel_files(folder_path, final_file_path)