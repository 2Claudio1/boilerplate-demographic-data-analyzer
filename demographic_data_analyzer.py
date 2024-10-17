import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    demographic_data_df = pd.read_csv('adult.data.csv')
    
    # Dataframe total length
    demographic_data_df_length = len(demographic_data_df)

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = demographic_data_df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round(demographic_data_df.loc[demographic_data_df['sex'] == 'Male', 'age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(((demographic_data_df['education'] == 'Bachelors').sum() / demographic_data_df_length) * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # Adds a column advanced-education to check if the person has advanced education
    demographic_data_df['advanced-education'] = demographic_data_df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = (demographic_data_df['advanced-education'])  # demographic_data_df['advanced-education'] == True
    lower_education = ~higher_education # demographic_data_df['advanced-education'] == False

    # percentage with salary >50K
    higher_education_rich = round((demographic_data_df[higher_education & (demographic_data_df['salary'] == '>50K')]['salary'].count() / demographic_data_df[higher_education]['salary'].count() * 100), 1)
    lower_education_rich = round((demographic_data_df[lower_education & (demographic_data_df['salary'] == '>50K')]['salary'].count() / demographic_data_df[lower_education]['salary'].count() * 100), 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = demographic_data_df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = (demographic_data_df['hours-per-week'] == min_work_hours).sum()

    rich_percentage = round((demographic_data_df.loc[(demographic_data_df['hours-per-week'] == min_work_hours) & (demographic_data_df['salary'] == '>50K')]['salary'].count() / num_min_workers) * 100, 1)

    # What country has the highest percentage of people that earn >50K?
    percentage_salary_bigger_50k_per_country = (demographic_data_df[demographic_data_df['salary'] == '>50K']['native-country'].value_counts() / demographic_data_df['native-country'].value_counts()) * 100
    
    highest_earning_country = percentage_salary_bigger_50k_per_country.idxmax()
    # Alternative approach to find the highest earning country using sorting
    #highest_earning_country = percentage_salary_bigger_50k_per_country.sort_values(ascending=False).head(1).index[0] #values[0]
    
    highest_earning_country_percentage = round(percentage_salary_bigger_50k_per_country.max(), 1)

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = (demographic_data_df[(demographic_data_df['salary'] == '>50K') & (demographic_data_df['native-country'] == 'India')])['occupation'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
