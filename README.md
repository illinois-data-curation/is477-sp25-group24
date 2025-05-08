# International Factors Impacting Life Expectancy
 is477-sp25-group24
 Copntributors: Alejandra Cornejo & Karolina Mikulec
 DOI:10.5281/zenodo.15368276
Link to Zenodo: https://zenodo.org/records/15368276

## Summary:
**Project Summary:**

This project investigates the global factors contributing to differences in life expectancy by examining the relationship between health expenditure, education, economic indicators, and access to healthcare. Using a merged dataset from the World Band and a global health and demographic dataset, we aim to investigate the economic disparities that influence population health across countries of varying income levels and developmental status. To do this analysis, we cleaned the data, primarily restructuring our JSON file and automated the visualizations created to do our analysis using a Snakemake pipeline and Python Scripts

**Motivation and Research Questions:**

	The driving factors of our analysis stem from trying to understand why life expectancy varies so widely across countries. Although life expectancy is influenced by numerous biological and environmental variables, we wanted to focus on economic and policy-driven factors such as healthcare access, public funding, and the economic conditions of the country as a whole. These choices were motivated by active real-world implications of public spending, especially in the mists of extreme budget cuts to essential programs in health and education from our government. We want to gain a bit more understanding of how funding levels for different programs may affect our overall well-being in the future. 

* What is the effect of education spending on life expectancy in low-income vs. high-income countries?
* How is access to healthcare related to life expectancy in countries of different economic statuses?
* Is life expectancy correlated with economic indicators like GDP?


    We chose to focus on nationwide effects instead of state-by-state differences as it shows us a dataset with larger ranges, although we do recognize this also invites a larger presence of confounding variables. This global scope, however, offers a broader lens through which to observe significant patterns and draw conclusions about the effects of economic policies on overall health.

**Contributions:**
    After creating a timeline and distributing responsibilities, we reflected and reassessed our contributions. Beginning in the first two weeks of the project, we equally spent time setting up the repository and finding datasets. Then, we spent time drafting a plan including research questions, a dataset analysis, a timeline, and our responsibilities. Then, looking at the third week, Alejandra took over cleaning and preparing the data while Karolina began the interim report. We both analyzed the code to discover any potential findings. In the fourth week, we both added visualizations or summaries and turned in the report. We had problems merging the data, however, Alejandra overcame that in the fifth week. Karolina and Alejandra met to work on the snake file in order to produce an automated workflow. In the sixth week, Karolina began the final report while Alejandra worked on any finishing touches. In the end, we finished all the documentations, posted to Zenodo, made sure licenses and citations were accurate, and archived the project. Overall, we worked efficiently and stayed on track by splitting the work evenly. We also found it easier to have Alejandra upload all materials to GitHub. 


 **Key Findings:**

	Our analysis showed many patterns between the chosen variables we analyzed. We primarily focused on variables within our merged dataset having to do with GDP, life expectancy, developmental status, and healthcare indexes such as the percentage of population with a variety of preventive vaccines, and average years of schooling. We found that High-income countries show a strong positive correlation between total health expenditure and life expectancy, with a tight cluster of data at the upper region of the graph. Low-income countries displayed a flatter relationship, suggesting that an increase in spending does not always directly increase life expectancy. This may be reflective of inefficiencies, lack of healthcare infrastructure, or lack of healthcare access. The computed correlation coefficient between healthcare access and life expectancy was 0.2955, indicating a moderate positive relationship. This is supported by the previous statement that improving healthcare spending and access doesn’t directly impact life expectancy, but is it still important. The average years of schooling are notably higher in both high-income and developed countries. The visualizations showed a tight clustering of these countries above most developing and low-income countries. The low-income and developing countries exhibited a larger variation within years and lower averages.

**Overview:**

	This project demonstrates that while higher levels of spending and access to services are associated with improved life expectancy, other factors and the context of the spending matter significantly. Increasing health budgets may not directly correlate to inefficiencies or inequalities within the healthcare system, but placing investments in a purposeful and impactful manner still remains highly important for the prosperity of a nation and its people. Our findings support the idea that sustainable investments in healthcare access, and health infrastructure are vital to increasing the overall well-being of a country, especially in developing countries. As governments debate budget priorities, this analytical insight serves as an important reminder that cutting funding to health and education could have severe long-term consequences on the prosperity of our overall country. 

## Data Profile:

    To provide an accurate analysis, we will provide a description of each dataset including license and terms of use. Starting with the World Bank Dataset, the format consists of a JSON file that was changed from an Excel file in order to make it easily integrated with the workflow. When looking at the scope of the dataset, it contains information regarding 264 countries/areas and has key variables like GDP/PPP, population, internet users, export of goods and services, life expectancy, and literacy rate. The source is https://data.worldbank.org/ which is the credible website for the World Bank Open Data. Furthermore, this dataset has a Creative Commons Attribution 4.0 license. So, it allows the data to be shared and modified if cited. This allows my partner and I to utilize it for academic purposes making the terms of use publicly available and reusable with credit. Overall, this dataset allows us to get a deeper look and build questions regarding the relationships between societal aspects like population, technology, and financials. We were able to make groups out of the countries based on whether they are leaning more towards a lower-income or higher-income country through GDP/PPP, exports, internet users, and literacy rate. Then, we can see the relationship between life expectancy and its influences on the economy. Next, we looked at the Health and Demographic Dataset. The format of the dataset is a CSV making it easy to work and perform analysis on. The scope of the dataset contains 133 countries ranging from 2000 to 2015. The key variables are life expectancy, the country’s development status, adult mortality, and infant death rates, health expenditures, different immunizations such as Polio, GDP, BMI, and the average amount of education. The data originates from the World Health Organization. However, I downloaded it from Kaggle, under the Creative Commons Public Domain license. The use of terms is open for academic analysis, changes, and collaboration with necessary citations when downloaded from Kaggle. Overall, this dataset tests how global factors influence life expectancy. In order to prepare our data for its intended use, we cleaned, merged, and double-checked the duplications in order to have an accurate amount of country-to-year data. We had difficulties merging the data at first, however, we utilized group by to merge by status. To conclude, both of our datasets let us gain perspectives on the finances and health of the countries being analyzed. The licenses are open and allow us to reproduce, copy, and collaborate on the data to explore impacts on life expectancy.

## Findings: 

	The driving factor of our analysis was to highlight disparities in health and education outcomes across a wide variety of countries with different income levels and developmental statuses. By examining total health expenditure in relation to life expectancy and years of schooling, we are able to understand more clearly trends that show the influence of the economic conditions of a country on the well-being of its citizens. 
	To begin our analysis we found it beneficial to analyze the health expenditure of a country vs. the average life expectancy of its citizens. We created two scatter plots comparing these two variables; one plot focusing on development status and the other on the GDP split between low and high income. When countries were split by status, developed and developing countries showed a very similar positive correlation slope, but there is a pronounced difference between the y-axis coordinates. This could suggest that developmental status can affect the efficiency and impact of healthcare expenditures since similar investments are producing lower average life expectancies within developing countries. When the same analysis was done but split between income levels based on GDP, countries considered high-income had a higher positively correlated slope than the lower-income countries. High-income countries also exhibited the same gap between the y-axis, again suggesting inefficiencies in investments, health infrastructure, or other confounding factors such as socioeconomic or environmental factors that impact life expectancy. The purpose of the same scatterplot without a regression line was to show that developed countries are tightly grouped toward the upper right portion of the graph while developing countries are more dispersed and often located in the lower ranges of the graph. This visual is supported by the calculated correlation coefficient of 0.2955 between the Healthcare Index and Life Expectancy, suggesting a moderate positive relationship.
	The following analysis focused on schooling highlights similar themes of inequities within countries. When comparing schooling by income level, high-income countries show higher and more consistent years of schooling, while low-income countries cluster at lower levels with more variation. The same pattern occurs when countries are split between developing and developed. Education is often seen as a driver for health literacy, economic potential, and civic engagement. When education is lower, it often has a significant impact on the well-being of a country's citizens and average economic growth. 
	During the analysis,  a bar chart showing the quantity disparity between developed and developing countries was included. The purpose of the graph is to convert a large imbalance of data, as developing countries make up a large percentage of the data. We chose to keep it as it reflects the world today, as it is made up of largely developing countries, with only a few being considered developed. 
	Overall, the data suggest that while investment in health and education is crucial for the overall well-being of the country's citizens, it is not equally effective across all countries. A country’s income level and development status is heavily influenced by how resources are utilized and what outcomes are achieved. The finding suggests increasing expenditure in certain areas isn’t enough to increase life expectancy. Although we realize many more factors should be considered when analyzing the possible increase of life expectancy in a country, the results help us understand that spending must be targeted towards a goal, effective and equitable to address systematic barriers in lower-income countries. 

## Future Work: 

    Looking back at our timeline of the project, the hardest portion we endured was the automation of analysis and merging of the data.  Because the duplicated data provided us with an inaccurate analysis at first, we learned about the importance of properly cleaning and preparing our data. The automation of analysis was the next challenge, although the analysis was pretty straightforward with many simple graphs outlining data patterns, automating it using a snakemake pipeline required being very attentive to where you store your data, how your data is structured, and how you name your data. Although we had done a snakmake file in class, most of the code was given, so making a file from scratch took a significant amount of work. Our first challenge was that our JSON file was in a raw form, to change it to an interpretable format we made a fix_json.py containing the following code 

    ```
    import json


    with open("data/world_bank_data.json", "r") as f:
    lines = f.readlines()


    parsed = [json.loads(line) for line in lines]


    with open("data/world_bank_data_fixed.json", "w") as f:
    json.dump(parsed, f, indent=2)


    print(" Converted raw JSON to valid JSON array.")

    ```
    After this, we ensured the proper libraries were downloaded for the results to generate and after what seemed like hundreds of attempts to run the snakemake file and tweak it each time it worked. This process was heavily aided by the structure of the labs and was executed with an extensive trial and error stage, especially during automation. Other than gaining technical advice, there are future findings we would like to look into based on the datasets we have. For example, we would like to make a model to analyze the overall health of future countries. These findings can help governments plan for action. Also, since the calculated correlation was fairly low, we would like to analyze a set of a variety of factors to find variables that have major impacts that were not included. Since life expectancy is a mix of socioeconomic, environmental, and political aspects, it might be beneficial to create an OLS regression equation to analyze many different factors within the same space.  Furthermore, we can look into comparing state or county-level relationships in order to see if there is even disbursement by county or state or if a certain trend is more condensed in certain places.

## Reproducing:
Instructions
**1.Set-Up**

Create a folder called `FinalProject` in your repository and an additional folder named `data` within it.  
Download the files from [this spreadsheet](https://docs.google.com/spreadsheets/d/1UmSFPXJuSwaATQc4uKovqFOWE43qGvdo/edit?usp=sharing&ouid=115773949683984374770&rtpof=true&sd=tru) and [this file](https://drive.google.com/file/d/1bX20gQbCFkYOnW3I10zUbc231xo1G5pu/view?usp=sharing), and extract them into the `FinalProject/data` folder.

**2.Change CSV to JSON**

Load the Excel file and then convert it to JSON so that it's easily transferable.

```
import pandas as pd

df = pd.read_excel('world_bank_data.xls')

print(df.head())

df.to_json('world_bank_data.json', orient='records', lines=True)
```

**3.Converting JSON into usable data**
In order to successfully merge the CSV data and the JSON data needs to be restructured in order to convert raw, line-by-line JSON into a structured, valid JSON array, making it usable for most JSON parsers and tools that expect an array format. Insert the following code to directly insert new cleaned data into your data folder already created 
```
import json


with open("data/world_bank_data.json", "r") as f:
    lines = f.readlines()


parsed = [json.loads(line) for line in lines]


with open("data/world_bank_data_fixed.json", "w") as f:
    json.dump(parsed, f, indent=2)


print(" Converted raw JSON to valid JSON array.")
```

**4.Creating analysis**
* Within your FinalProject main branch, create a file named analyze_data.py
* import required libraries to run analysis this includes
```
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.formula.api as smf
import os
import json
```
**5.Merging Data:**
Read the data into data frames, do simple cleaning, and make sure to limit the data to 2014 data for Life Expectancy data. You can do this by submitting the following code 
```
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
```
**6.Creating visualizations:**
* Within your analyze_data.py Input the following code to output the visualizations we are using to do our primary analysis on.
```
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
```
* All of the following statements are simply many different visualizations out into a large order 

**7.Preparing for automation:**
* Add a statement at the bottom of your analyze_data.py that serves as a data analysis pipeline that, loads and cleans data, plots the charts, and computes the correlation
```
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
```
**8.Creating SnakeFile:**
* Create a SnakeFile within your FinalProject main repository 
* Within this SnakeFile creates rules that have an input, which is your data and the output specifies the raw input files needed for analysis.
```
rule all:
    input:
        "results/schooling_status.png",
        "results/schooling_income.png",
        "results/status_count.png",
        "results/health_vs_lifeexp_status.png",
        "results/health_vs_lifeexp_income.png",
        "results/healthcare_access_vs_lifeexp.png",
        "results/correlation.txt"

rule run_analysis:
    input:
        "data/Life_Expectancy_Data.csv",
        "data/world_bank_data.json"
    output:
        "results/schooling_status.png",
        "results/schooling_income.png",
        "results/status_count.png",
        "results/health_vs_lifeexp_status.png",
        "results/health_vs_lifeexp_income.png",
        "results/healthcare_access_vs_lifeexp.png",
        "results/correlation.txt"
    script:
        "analyze_data.py"
```
**Running Automation of workflow**
* Within your terminal make sure to cd your FinalProject folder, write snakemake –cores 1
* You will know if your rules ran successfully if you have a new file in your repository called results with different PNG and Txt files of the results produced. 

**10.Final Analysis:**
* Look through your results folder and analyze what the results tell you and come to conclusions based on initial questions.

## References:
World Bank Open Data. (2024). https://data.worldbank.org
WHO Health Statistics (via Kaggle). https://www.kaggle.com/datasets/kumarajarshi/life-expectancy-who
Snakemake. Köster J, Rahmann S. (2012) Bioinformatics. https://snakemake.readthedocs.io
Pandas Development Team (2024). pandas-dev/pandas: Pandas. https://doi.org/10.5281/zenodo.3509134



