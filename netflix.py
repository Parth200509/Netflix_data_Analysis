# import pandas as pd

# # STEP 1: Data load karo
# df = pd.read_csv(r"C:\Users\parth\Downloads\netflix_titles_CLEANED.csv")   # <-- yahan apni file ka naam daal

# # STEP 2: Basic info
# print("🔹 Data Info:")
# print(df.info())

# print("\n🔹 First 5 rows:")
# print(df.head())

# # STEP 3: Empty strings ko NaN me convert karo
# df.replace("", pd.NA, inplace=True)

# # STEP 4: Missing values count (column-wise)
# print("\n🔹 Missing Values Count (Column-wise):")
# missing = df.isnull().sum()
# print(missing)

# # STEP 5: Sirf wo columns jisme missing hai
# print("\n🔹 Columns with Missing Values:")
# print(missing[missing > 0])

# # STEP 6: Missing percentage
# print("\n🔹 Missing Percentage (%):")
# missing_percent = (df.isnull().sum() / len(df)) * 100
# print(missing_percent[missing_percent > 0])

# # STEP 7: Rows jahan koi bhi value missing hai
# print("\n🔹 Rows with Missing Values:")
# print(df[df.isnull().any(axis=1)])

# # STEP 8: (Optional) Drop rows with missing values
# df_cleaned = df.dropna()

# # STEP 9: (Optional) Fill missing values
# # Example: numeric columns ke liye mean
# df_filled = df.fillna(df.mean(numeric_only=True))

# # STEP 10: Cleaned data save karo
# df_cleaned.to_csv("cleaned_data.csv", index=False)

# print("\n✅ Data cleaning complete & saved as 'cleaned_data.csv'")

import pandas as pd

# STEP 1: Data load
df = pd.read_csv("C:/Users/parth/Downloads/netflix_titles_CLEANED.csv")

# STEP 2: Check missing values
print("🔹 Missing Values Before Cleaning:")
print(df.isnull().sum())

# STEP 3: Delete rows with any null values
df_cleaned = df.dropna()

rows_with_null = df[df.isnull().any(axis=1)]
print(rows_with_null.shape)

# STEP 4: Check again
print("\n🔹 Missing Values After Cleaning:")
print(df_cleaned.isnull().sum())

# STEP 5: Shape check (kitna data delete hua)
print("\n🔹 Before:", df.shape)
print("🔹 After:", df_cleaned.shape)

# STEP 6: Save cleaned file
df_cleaned.to_csv("C:/Users/parth/Downloads/netflix_cleaned_final.csv", index=False)

print("\n✅ Cleaning complete! File saved as 'netflix_cleaned_final.csv'")