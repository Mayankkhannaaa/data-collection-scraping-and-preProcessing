# imporing pandas
import pandas as pd
import numpy as np
import json

# Uncomment desired lines of code and use it as per requirement 🚀

# Importing dataset
# df = pd.read_csv('my_table.csv')

df = pd.read_csv("revised_data.csv")
original_shape = df.shape

# Size of original dataset
# print(df.shape)

# Dropping the missing rows.
# df_dropped = df.dropna(how = 'any')
# print(df_dropped.shape)
# df_dropped.to_csv('cleaned_data.csv', index=False)

# Dropping rows where column 'my_column' is not an integer
# df_dropped = df[df['Price'].apply(lambda x: print("text w/0 comma: ", x.replace(',', ''),"Using instance for int: ", isinstance(int(x.replace(',', '')), int),"Usomg isDig: ", x.replace(',', '').isdigit(), "Using insta of float: ",isinstance(float(x.replace(',', '')), float))or isinstance(x.replace(',', ''), int) or x.replace(',', '').isdigit())]
# print(df_dropped.shape)


# df['Price'] = df['Price'].str.replace(',', '')
# Convert column to numeric data types
# df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

# Drop rows with invalid values
# df = df.dropna(subset=['Price'])
# print(df.shape)

# Save cleaned data to a new CSV file
# df.to_csv('cleaned_data.csv', index=False)

# print(df['Price'].dtype)

# df['Price'] = df['Price'].str.replace(',', '')

# Filter 'my_column' column by 'object' data type and remove missing values
# df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

# str_values = df[df['Price'].apply(lambda x: isinstance(x, (int,float)))]

# print(str_values,len(str_values))

# str_values.to_csv('cleaned_data.csv', index=False)

# Remove rows where any column has a value equal to "Previous page"
# df = df[~(df == 'Previous page').any(axis=1)]
# df.to_csv('cleaned_data.csv', index=False)

# df = pd.read_csv('my_table.csv')

# Extracting decimal numbers from the column values
# df['AvgRating'] = df['AvgRating'].str.extract('(\d+\.\d+)', expand=False).astype(float)

# Print updated dataset
# print(df)
# df.to_csv('cleaned_data.csv', index=False)
# print(df['AvgRating'].dtype,df['TotalRatings'].dtype)

# df['Features'] = df['Features'].str.replace('"', "'")
# df.to_csv('cleaned_data1.csv', index=False)


# Extract the unique keys from the JSON column
# unique_keys = set()
# good_data = []
# for idx, json_str in enumerate(df["Features"]):
# try:
#     json_str = json_str.replace("'", '"')
#     json_obj = json.loads(json_str)
#     unique_keys.update(json_obj.keys())
#     good_data.append(df.loc[idx])
# except json.JSONDecodeError as e:
#     # print(f"Error at row {idx}: {e}")
#     x = df.loc[idx, "Features"]
#     y = df.loc[idx + 1, "Features"]
#     # print("line 77",x)
#     # print("line 78",y)
#     new_x = x.split(",")
#     new_y = y.split(",")
#     lol = x.replace(",", "@")
#     # print(len(new_x),len(new_y))
#     # print("line 79",json.loads(df.loc[idx,'Features'].replace("'", "\"")))
#     # print("line 80",json.loads(y.replace("'", "\"")))
#     # print("line 89",lol)
#     pass

# Print the unique keys
# print("Unique keys: ", len(unique_keys))

# for key in unique_keys:
#     df[key] = pd.Series(dtype=str)

# # Iterate over each row and extract the values for each key
# for i, row in df.iterrows():
#     json_str = row["Features"].replace("'", '"')
#     json_obj = json.loads(json_str)
#     for key in unique_keys:
#         if key in json_obj:
#             df.at[i, key] = json_obj[key]

# print(original_shape, df.shape)

# df.to_csv("cleaned_data2.csv", index=False)

# good_df = pd.DataFrame(good_data)
# good_df.to_csv('cleaned_data1.csv', index=False)

# Print the unique keys
# print(unique_keys)


# df["AvgRating*TotalRating"] = df["AvgRating"] * df["TotalRatings"]
# print(original_shape, df.shape)

# max_val = df["AvgRating*TotalRating"].max()
# df["Label"] = df["AvgRating*TotalRating"] / max_val
# df.to_csv("revised_data.csv", index=False)
# df = df.fillna(
#     df.dtypes.replace("object", "missing")
#     .replace("bool", None)
#     .replace("int", np.nan)
#     .replace("float", np.nan)
# )
# df.to_csv("revised_data.csv", index=False)
