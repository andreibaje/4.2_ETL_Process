import pandas as pd
import os

countries = ["USA", "Russia", "UK", "South Korea"]
output_folder = "result"
os.makedirs(output_folder, exist_ok=True)
df = pd.read_csv("movies.csv")
df.columns = df.columns.str.strip().str.lower()
df["budget"] = pd.to_numeric(df["budget"].replace('[\$,]', '', regex=True), errors='coerce')
df["box_office"] = pd.to_numeric(df["box_office"].replace('[\$,]', '', regex=True), errors='coerce')
df["bilanț"] = df["box_office"] - df["budget"]
for country in countries:
    df_country = df[df["country"] == country]
    df_country = df_country.drop(columns=["language", "country", "duration", "budget", "box_office"], errors="ignore")
    df_filtered = df_country[["title", "release_year", "genre", "director", "bilanț"]].copy()
    df_filtered = df_filtered.sort_values(by="bilanț", ascending=False)
    top_10 = df_filtered.head(10)
    name_file = f"{country.replace(' ', '_')}_top_10.xlsx"
    path_file = os.path.join(output_folder, name_file)
    top_10.to_excel(path_file, index=False)

print("The files have been made in the folder 'output'.")