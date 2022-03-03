# noinspection PyUnresolvedReferences
import pandas as pd
# noinspection PyUnresolvedReferences
import numpy as np
df = pd.read_csv("S:\\ML_AI_DS\\MY_TASKS\\Income_expense.csv")
print(df)  # To check how the dataset has been imported
df1 = df[["income", "expense"]]
# TO-DO
# Create a function that subtracts two columns in the dataframe
# Create a new column "savings" and put the resulting output in that column for all values


def savings(a, b):
    return(a-b)


df1['savings'] = df1.apply(lambda f: savings(f['income'], f['expense']), axis=1)
print(df1)