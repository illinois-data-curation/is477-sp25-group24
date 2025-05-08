
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.formula.api as smf
import os
import json

os.makedirs("results", exist_ok=True)

def load_and_prepare_data():
    with open("data/world_bank_data_fixed.json") as f:
        dev_raw = json.load(f)
    dev_df = pd.DataFrame(dev_raw)

    health_df = pd.read_csv("data/Life_Expectancy_Data.csv", thousands=",")
    health_df = health_df[health_df["Year"] == 2014]

    dev_df.rename(columns={"Country Name": "Country"}, inplace=True)
    dev_df.dropna(subset=["Country"], inplace=True)

    df = pd.merge(health_df, dev_df, on="Country")
    df["Income Level"] = pd.qcut(df["GDP, PPP (current international $)"], q=2, labels=["Low Income", "High Income"])

    return df


    df["Income Level"] = pd.qcut(df["GDP, PPP (current international $)"],
                                  q=2,
                                  labels=["Low Income", "High Income"])

    return df  

def plot_schooling_by_status(df):
    plt.figure(figsize=(10, 6))
    sns.stripplot(data=df, x="Status", y="Schooling", hue="Status", palette={"Developing": "skyblue", "Developed": "coral"})
    plt.title("Schooling by Development Status")
    plt.savefig("results/schooling_status.png")
    plt.close()

def plot_schooling_by_income(df):
    plt.figure(figsize=(10, 6))
    sns.stripplot(data=df, x="Income Level", y="Schooling", hue="Income Level", palette={"Low Income": "lightgreen", "High Income": "orange"})
    plt.title("Schooling by Income Level")
    plt.savefig("results/schooling_income.png")
    plt.close()

def plot_status_counts(df):
    plt.figure(figsize=(8, 6))
    sns.countplot(data=df, x="Status", palette={"Developing": "skyblue", "Developed": "coral"})
    plt.title("Number of Developed vs Developing Countries")
    plt.savefig("results/status_count.png")
    plt.close()

def plot_health_vs_lifeexp_by_status(df):
    sns.lmplot(data=df, x="Total expenditure", y="2014 Life expectancy at birth, total (years)", hue="Status", palette={"Developing": "skyblue", "Developed": "coral"})
    plt.title("Health Expenditure vs. Life Expectancy by Development Status")
    plt.savefig("results/health_vs_lifeexp_status.png")
    plt.close()

def plot_health_vs_lifeexp_by_income(df):
    sns.lmplot(data=df, x="Total expenditure", y="2014 Life expectancy at birth, total (years)", hue="Income Level", palette={"Low Income": "lightgreen", "High Income": "orange"})
    plt.title("Health Expenditure vs. Life Expectancy by Income Level")
    plt.savefig("results/health_vs_lifeexp_income.png")
    plt.close()

def plot_healthcare_access(df):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x="Total expenditure", y="2014 Life expectancy at birth, total (years)", hue="Status")
    plt.title("Healthcare Access vs Life Expectancy")
    plt.savefig("results/healthcare_access_vs_lifeexp.png")
    plt.close()

def compute_correlation(df):
    corr = df[["Total expenditure", "2014 Life expectancy at birth, total (years)"]].corr().iloc[0,1]
    with open("results/correlation.txt", "w") as f:
        f.write(f"Correlation between Healthcare index and Life Expectancy: {corr:.4f}\n")

def main():
    df = load_and_prepare_data()
    plot_schooling_by_status(df)
    plot_schooling_by_income(df)
    plot_status_counts(df)
    plot_health_vs_lifeexp_by_status(df)
    plot_health_vs_lifeexp_by_income(df)
    plot_healthcare_access(df)
    compute_correlation(df)

if __name__ == "__main__":
    main()