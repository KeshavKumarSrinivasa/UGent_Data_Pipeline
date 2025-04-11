import pandas as pd
import processing_functions

# Aggregate all the steps
def process_raw_data(df, columns_to_sort, excluded_beverages_list):
    df = processing_functions.sort_data(df, columns_to_sort)
    df = processing_functions.add_beverage_consumed_column(df)
    df = processing_functions.add_energy_contrib_column(df)
    df = processing_functions.add_percent_contrib_totenergy_column(df)
    df = processing_functions.add_ssb_consumed_column(df, excluded_beverages_list)
    df = processing_functions.add_age_category_column(df)
    return df



if __name__ == "__main__":
	# Load Data
	input_path = "dataset/raw/raw_synthetic_motherfile_dietary_data.xlsx"
	output_path = "dataset/processed/processed_motherfile_dietary_data.xlsx"
	input_df = pd.read_excel(input_path)

	# Set the argument values
	columns_to_sort = ["ennsbiocode","eacode","hcn"]
	excluded_beverages = ["BUKO PALAMIG","CARBONATED BEVERAGE","CHOCOLATE BEVERAGE","CHOCOLATE DRINK","CHOCOLATE MILK DRINK","COFFEE","COKE/COLA","ENERGEN DRINK","ENERGY DRINK","ENERGY DRINKS","FRUIT DRINK","FRUIT JUICE","FRUIT JUICE , DRINK","FRUIT JUICE DRINK","GULAMAN PALAMIG","ICED TEA","JUICE","JUICE DRINK","JUICE DRINKS","LEMON TEA DRINK","MILK TEA","MILKTEA","MINUTE MAID","ORANGE JUICE","PALAMIG","PALAMIG NA SAGO","PINEAPPLE JUICE","SAGO PALAMIG","SOFRDINKS","SOFT DRINK","SOFT DRINKKS","SOFT DRINKS","SOFTDR INKS","SOFTDRINK","SOFTDRINKS","SOFTDRINKS,","SOFTDRINS","SOFTDRNKS","SUGAR","TEA","TEA DRINK","TEA DRINKS","TEADRINK"]

	# process data
	processed_df = process_raw_data(input_df,columns_to_sort,excluded_beverages)

	# Save cleaned data
	processed_df.to_excel(output_path,index = False)