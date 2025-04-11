import pandas as pd
import numpy as np

# Sort the dataset based on given columns
def sort_data(input_df, columns_to_sort):
    return input_df.sort_values(by=columns_to_sort)


# Add a 'beverage_consumed' column based on rf_code == 7
def add_beverage_consumed_column(input_df):
    input_df = input_df.copy()
    input_df["beverage_consumed"] = input_df["rf_code"].apply(lambda x: 1 if x == 7 else 0)
    return input_df


# Add a 'energy_contrib_all_beverage' column based on 'Energy' column
def add_energy_contrib_column(input_df):
    input_df = input_df.copy()
    input_df["energy_contrib_all_beverage"] = input_df["Energy"]
    return input_df


# Add a '%contrib_totenergy' column based on 'Energy' and 'Total Energy (Kcal)' column
def add_percent_contrib_totenergy_column(input_df):
    input_df = input_df.copy()
    input_df["%contrib_totenergy"] = (input_df["Energy"] / input_df["Total Energy"]) * 100
    return input_df

# Add a 'ssb_consumed' column based on 'bevarage_consumed' and excluded list of beverages
def add_ssb_consumed_column(input_df,excluded_beverages_list):
    input_df = input_df.copy()

    is_not_excluded = ~input_df["food_item"].isin(excluded_beverages_list)

    input_df["ssb_consumed"] = (input_df["beverage_consumed"] == 1) & is_not_excluded
    input_df["ssb_consumed"] = input_df["ssb_consumed"].astype(int)

    return input_df

# Add "age_category" column based on "age" column
def add_age_category_column(input_df):
    input_df = input_df.copy()

    bins = [0,6,10,19,59,np.inf]
    labels = ["Under 6", "Children", "Adolescents", "Adults", "Elderly"]


    input_df["age_category"] = pd.cut(input_df["age"],bins=bins,labels=labels, right = True)

    return input_df

