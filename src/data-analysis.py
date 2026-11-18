import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_DIR / "data"
VISUALIZATION_DIR = PROJECT_DIR / "visualizations"

VISUALIZATION_DIR.mkdir(exist_ok=True, parents=True)

DATA_FILE= DATA_DIR / "annual-temperature-anomalies.csv"

df = pd.read_csv(DATA_FILE)

print("\nDATASET OVERVIEW")
print("----------------")
print("Original dataset shape:", df.shape)

print("\nMissing values in original dataset:")
print(df.isnull().sum())

world = df[df["Entity"] == "World"].copy()

world = world.sort_values("Year").reset_index(drop=True)
print("\nGLOBAL DATASET SUMMARY")
print("----------------------")
print("Number of records:", len(world))
print("Year range:", world["Year"].min(), "-", world["Year"].max())

print("World Dataset Shape", world.shape)

print("Missing values in World Dataset :")
print(world.isnull().sum())


mean_temp = world["Temperature anomaly"].mean()
median_temp = world["Temperature anomaly"].median()

min_temp = world["Temperature anomaly"].min()
max_temp = world["Temperature anomaly"].max()

min_year = world.loc[
    world["Temperature anomaly"].idxmin(), "Year"
]

max_year = world.loc[
    world["Temperature anomaly"].idxmax(), "Year"
]

print("\nSTATISTICAL ANALYSIS")
print("--------------------")
print(f"Mean anomaly: {mean_temp:.4f}")
print(f"Median anomaly: {median_temp:.4f}")
print(f"Minimum anomaly: {min_temp:.4f} ({min_year})")
print(f"Maximum anomaly: {max_temp:.4f} ({max_year})")

print("\nEARLIEST GLOBAL RECORDS")
print("-----------------------")
print(world[["Year", "Temperature anomaly"]].head().to_string(index=False))

print("\nLATEST GLOBAL RECORDS")
print("---------------------")
print(world[["Year", "Temperature anomaly"]].tail().to_string(index=False))

plt.figure(figsize =(12,6))

plt.plot(
    world["Year"],
    world["Temperature anomaly"],
    linewidth =2,
    label ="Global Temperature Anomaly",
)

plt.title("Global Temperature Anomaly (1940 - 2025)")
plt.xlabel("Year")
plt.ylabel("Temperature anomaly (°C)")

plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig(VISUALIZATION_DIR / "global_temp_anomaly.png", dpi=300)
plt.show()


recent_years = world.tail(10)
plt.figure(figsize =(12,6))

plt.bar(
    recent_years["Year"],
    recent_years["Temperature anomaly"],
    label="Temperature anomaly"
)

plt.title("Global Temperature Anomaly (Last 10 Years)")
plt.xlabel("Year")
plt.ylabel("Temperature anomaly (°C)")

plt.grid(axis ='y',alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig(VISUALIZATION_DIR / "recent_temperature_comparison.png", dpi=300)
plt.show()


correlation = world["Year"].corr(
    world["Temperature anomaly"]
)

print("\nCORRELATION ANALYSIS")
print("--------------------")
print(f"Year and temperature anomaly: {correlation:.4f}")