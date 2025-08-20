import pandas as pd
import matplotlib.pyplot as plt

INDUSTRY_TARGET = 4.5

def main():
    df = pd.read_csv("quarterly_data.csv")
    avg = df["Patient_Satisfaction_Score"].mean().round(2)
    print(f"Average Patient Satisfaction Score (2024): {avg}")

    # Save simple stats
    stats = {
        "average": float(avg),
        "min": float(df["Patient_Satisfaction_Score"].min()),
        "max": float(df["Patient_Satisfaction_Score"].max()),
        "industry_target": INDUSTRY_TARGET
    }
    import json
    with open("summary.json", "w") as f:
        json.dump(stats, f, indent=2)

    # Visualization
    plt.figure(figsize=(8,5))
    plt.plot(df["Quarter"], df["Patient_Satisfaction_Score"], marker="o")
    plt.axhline(INDUSTRY_TARGET, linestyle="--")
    plt.title("Patient Satisfaction Score - 2024 Quarterly Trend")
    plt.xlabel("Quarter")
    plt.ylabel("Score")
    for x, y in zip(df["Quarter"], df["Patient_Satisfaction_Score"]):
        plt.text(x, y, f"{y:.2f}", ha="center", va="bottom")
    plt.tight_layout()
    plt.savefig("chart.png", dpi=150)

if __name__ == "__main__":
    main()