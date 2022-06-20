import pandas as pd

dataframe = pd.read_csv("output.txt", error_bad_lines=False)

dataframe.to_csv("converted.csv", index= None)
