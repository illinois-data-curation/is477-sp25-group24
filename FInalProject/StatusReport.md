
# Final Project Mid Status Report 
Alejandra Cornejo & Karolina Muleck 

## ReCap

Throughout the Project, our main purpose is to take different datasets with factors such as gdp, education, healthcare accessibility, etc., to understand the following questions: What is the effect of education spending on life expectancy in low-income vs. high-income countries? How is access to healthcare related to life expectancy in countries of different economic status? Is life expectancy correlated with economic indicators like GDP per capita and unemployment rates across countries?We have tackled these questions by analyzing the Health and Demographics Dataset and the World Bank Dataset in order to provide us with international demographic data analysis and statistics. 

## Update on Tasks 

Our primary focus so far has been cleaning the data, merging the different datasets, and conducting some analysis on our merged dataset. Since each datase contained unique variables that contribute to the holistic understanding of each country, combining them allows for more streamlined and meaningful analysis. The merged dataset include the following variables:
[Country Name', 'Region Code', 'Country Code',
       'GDP, PPP (current international $)', 'Population, total',
       'Population CGR 1960-2015', 'Internet users (per 100 people)',
       'Popltn Largest City % of Urban Pop',
       '2014 Life expectancy at birth, total (years)',
       'Literacy rate, adult female (% of females ages 15 and above)',
       'Exports of goods and services (% of GDP)', 'Country', 'Year', 'Status',
       'Life expectancy ', 'Adult Mortality', 'infant deaths', 'Alcohol',
       'percentage expenditure', 'Hepatitis B', 'Measles ', ' BMI ',
       'under-five deaths ', 'Polio', 'Total expenditure', 'Diphtheria ',
       ' HIV/AIDS', 'GDP', 'Population', ' thinness  1-19 years',
       ' thinness 5-9 years', 'Income composition of resources', 'Schooling']
After completing the medge, we developed various visualizations and metrics to explore the relationship outlined in our research questions. One of our first findings was the clear disparity in average education levels between deleped and developing countries. The result showed the average education level is about 4 years higher in developed countries than developing countries. Bulding on this, we investigated the relationship between national investment and life expectancy. We used scatter plots with lines of best fit and found a positive correlation, with a coefficient of approximately 0.43. However, we also observed that countries with similar investment levels, developed nations still exhibited higher life expectancy, This suggests that while investment is relevant, it is not the most important factor that determines life expectancy, other systemic , structural, or environmental factors are likely to contribute to this disparity. Instead of only looking at countries through developed and non developed, we created a threshold that separates countries between "low income" and "high income". Countries with a GDP lower than 2 where considered low income and countries with GDP higher than 2 where considered high income. This reclassification causes some countries previously marked as developed to fall under the low income category. We then examines the basic healthcare outcomes, particularly vaccination reates for prevalent diseases, and compared them to life expectancy. Using color coded plots, we where able to differentiate low income countries for high income countries. Once again, the high-income countries consistently demonstrated higher life expectancy, even if the vaccination rates where similar. 



## Updated Timeline

When looking at the progress of our timeline, up until this week it has been accurate and up to date. In the first week which was March 9th - March 15th, we were successful in picking our partners and in creating a Github repository including the two of us. The second week is March 30th - April 5th and it went as planned since we submitted an initial project plan that consisted of the subject and datasets we chose. However, a setback we encountered during this process was that our Github repository was not created within the illinois-data-curation repository, but we updated the link and got it fixed. For the third week ranging from April 6th - April 12th, the task was to prepare the data, profile, assess, integrate, and clean it in preparation for analysis. The analysis was completed, but we encountered some problems with merging the data which is a change we have to make based on our progress. In the fourth week, from April 13th - 19th, we worked on the status report and were focusing on the visualizations and beginning stages of the project. However, because of the data merging and duplication issue, we stopped analysis and worked on fixing the code and adding to it. Furthermore, the fifth week is April 20th - April 26th where Alejandra will work on the automated workflows and where Karolina will document them. Moreover, since the deadline got extended, we will spend the sixth week (April 27th - May 3rd) making any finishing touches to the project by cleaning up the data and making sure it is presented neatly and efficiently rather than uploading as stated in the preliminary plan. Ultimately, the last week is May 4th - May 8th where Karolina will finish all the documentations, post to Box, make sure license and citations are accurate, create a metadata, and archive the project. All in all, having a timeline is important to make sure we stay on track and provide a great quality of work.




## Description of Changes based on Progress 

While our timeline has been on track, we have run into one main problem when cleaning and merging the datasets. The problem lies in the merging of the developing and developed countries column. When coding a bar graph to show the discrepancy between the two types, we have realized that developing countries have a row count of 1407 and developed countries have a row count of 242, which is out of reach since there are only 195 countries in the world. This is a problem because the datasets include more information regarding the developing countries making the test statistics and data distribution skewed. We did not realize the error the first time around, so our timeline will have to adjust to incorporate the fixing of this dataset analysis to get rid of duplicates and to only count the country once. In order to fix this change, we need to de-duplicate and make sure each country and year are accounted for once. Then, we need to re-filter and add the data correctly ensuring that there are no duplicates. Furthermore, looking at our timeline, after submitting the report, we will take a step back and remerge and fix the data and analysis rather than continuing with the visualizations and deep analysis that was expected as per the timeline. All in all, we are on track to finishing the project on time and answering our overarching research questions. 
