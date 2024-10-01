import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\91948\Downloads\API_SP.POP.TOTL_DS2_en_csv_v2_31753 (1)\API_SP.POP.TOTL_DS2_en_csv_v2_31753.csv", skiprows=4)

print(df.head())

df_2020 = df[['Country Name', '2020']].dropna()

df_2020 = df_2020.sort_values(by='2020', ascending=False)

top_10_countries = df_2020.head(10)

plt.figure(figsize=(10, 6))
plt.bar(top_10_countries['Country Name'], top_10_countries['2020'], color='skyblue')
plt.xlabel('Country')
plt.ylabel('Population in 2020')
plt.title('Top 10 Countries by Population in 2020')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
