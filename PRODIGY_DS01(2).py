import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Country Name': ['USA', 'China', 'India', 'Brazil', 'Russia'],
    'Male Population': [162000000, 730000000, 710000000, 103000000, 71000000],
    'Female Population': [169000000, 708000000, 680000000, 109000000, 74800000]
}


df = pd.DataFrame(data)

plt.figure(figsize=(10, 6))
plt.bar(df['Country Name'], df['Male Population'], label='Male Population', color='lightblue')
plt.bar(df['Country Name'], df['Female Population'], label='Female Population', bottom=df['Male Population'], color='pink')

plt.xlabel('Country')
plt.ylabel('Population')
plt.title('Gender Distribution by Country in 2020')
plt.xticks(rotation=45)
plt.legend()

plt.tight_layout()
plt.show()
