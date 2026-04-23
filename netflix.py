import pandas as pd
df = pd.read_csv("C:/Users/parth/Downloads/netflix_titles_CLEANED.csv")

print("🔹 Missing Values Before Cleaning:")
print(df.isnull().sum())

df_cleaned = df.dropna()

rows_with_null = df[df.isnull().any(axis=1)]
print(rows_with_null.shape)

print("\n🔹 Missing Values After Cleaning:")
print(df_cleaned.isnull().sum())

print("\n🔹 Before:", df.shape)
print("🔹 After:", df_cleaned.shape)

df_cleaned.to_csv("C:/Users/parth/Downloads/netflix_cleaned_final.csv", index=False)

print("\n✅ Cleaning complete! File saved as 'netflix_cleaned_final.csv'")
