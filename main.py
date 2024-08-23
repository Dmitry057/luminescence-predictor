import pandas as pd
train_dataset_path = 'train_split_fluor.csv'

train_dataframe = pd.DataFrame(pd.read_csv(train_dataset_path))

print(train_dataframe.head())