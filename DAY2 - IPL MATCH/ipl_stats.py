import pandas as pd 
# Load CSV
df = pd.read_csv("ipl.csv")
df1= pd.read_csv("deliveries.csv")

print("\n=== Loaded IPL Dataset ===")
print(df.head())

# 1️⃣ Top 3 Run Scorers
top_scorers = (
    df.groupby("batsman")["runs"]
    .sum()
    .sort_values(ascending=False)
    .head(3)
)

print("\n🏆 Top 3 Run Scorers:")
print(top_scorers)


# 2️⃣ Strike Rate > 140
df["strike_rate"] = (df["runs"] / df["balls"]) * 100

high_sr = df[df["strike_rate"] > 140][["batsman", "runs", "balls", "strike_rate"]]

print("\n⚡ Players with Strike Rate > 140:")
print(high_sr)


# 3️⃣ Most Boundaries (4s + 6s)
df["boundaries"] = df["fours"] + df["sixes"]

boundary_leaders = (
    df.groupby("batsman")["boundaries"]
    .sum()
    .sort_values(ascending=False)
    .head(3)
)

print("\n🔥 Players with Most Boundaries:")
print(boundary_leaders)


# DAILY CHALLENGE
# 4️⃣ Team With Highest Total Runs Combined
team_runs = (
    df.groupby("team")["runs"]
    .sum()
    .sort_values(ascending=False)
    .head(1)
)
print("\n💥 Team with Highest Total Runs:")
print(team_runs)


