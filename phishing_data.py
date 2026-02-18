from transformers import DistilBertTokenizerFast
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import pandas as pd

file_path = "/Users/seungjooyoon/local/code/github/cloned/PhishingSpamDataSet/4_MergeDataSet/merged_all_emails.csv"

df = pd.read_csv(file_path, index_col=0) # (12,300, 12)
#df_body = df["Body"]
# print(set(df["Type"])) # 'Phishing', 'Spam', 'Valid' 'Phishing simulation' What are the differences between them?
print(df.head())
print(df.sample(10))
print(df.describe())
print(df.describe(include="all"))

print(df.dtypes)
print(df.columns)
print(df.info())

print(set(df["Type"]))


# Data preparation

