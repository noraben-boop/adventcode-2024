import pandas as pd

location_list = pd.read_csv('day1_task1.csv')

first_list = location_list.iloc[:, 0].sort_values().reset_index(drop=True)
second_list = location_list.iloc[:, 1].sort_values().reset_index(drop=True)



