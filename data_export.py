import pandas as pd

df = pd.read_csv("new_club_data_test_pro.csv")
df.dropna(how="all", inplace=True)
df.drop_duplicates(subset=["Club Name"], inplace=True)
df.to_csv("new_club_data_test_pro.csv", index=False)
