import pandas as pd

file_path = "/Users/seungjooyoon/local/code/github/cloned/PhishingSpamDataSet/4_MergeDataSet/merged_all_emails.csv"

df = pd.read_csv(file_path, index_col=0) # (12,300, 12)
#df_body = df["Body"]
print(set(df["Type"])) # 'Phishing', 'Spam', 'Valid' What are the differences between them?
