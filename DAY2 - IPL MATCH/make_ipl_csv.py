import pandas as pd

df = pd.read_csv("deliveries.csv")

print("Original columns:", df.columns.tolist())

ipl = pd.DataFrame()

ipl["batsman"] = df["batter"]    
ipl["runs"] = df["batsman_runs"]
ipl["balls"] = 1
ipl["fours"] = df["batsman_runs"].apply(lambda x: 1 if x == 4 else 0)
ipl["sixes"] = df["batsman_runs"].apply(lambda x: 1 if x == 6 else 0)
ipl["team"] = df["batting_team"]

ipl.to_csv("ipl.csv", index=False)

print("\nCreated ipl.csv successfully!")
print(ipl.head())
