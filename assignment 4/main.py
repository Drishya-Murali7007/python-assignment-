import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("weather_data.csv")
print("HEAD:")
print(df.head())
print("\nINFO:")
print(df.info())
print("\nDESCRIBE:")
print(df.describe())
 
df = df.dropna(how="all")
df = df.fillna(method="ffill")
df['date'] = pd.to_datetime(df['date'])

df = df[['date', 'temperature', 'humidity', 'rainfall']]


temp = df['temperature'].to_numpy()

print("\nSTATISTICS:")
print("Mean:", np.mean(temp))
print("Max:", np.max(temp))
print("Min:", np.min(temp))
print("Std Dev:", np.std(temp))


plt.figure(figsize=(10,5))
plt.plot(df['date'], df['temperature'])
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.title("Daily Temperature Trend")
plt.savefig("daily_temperature.png")
plt.show()


df['month'] = df['date'].dt.month
monthly_rain = df.groupby('month')['rainfall'].sum()

plt.figure(figsize=(10,5))
plt.bar(monthly_rain.index, monthly_rain.values)
plt.xlabel("Month")
plt.ylabel("Total Rainfall")
plt.title("Monthly Rainfall")
plt.savefig("monthly_rainfall.png")
plt.show()

plt.figure(figsize=(8,5))
plt.scatter(df['temperature'], df['humidity'])
plt.xlabel("Temperature")
plt.ylabel("Humidity")
plt.title("Humidity vs Temperature")
plt.savefig("humidity_vs_temperature.png")
plt.show()


plt.figure(figsize=(12,6))

plt.subplot(1, 2, 1)
plt.plot(df['date'], df['temperature'])
plt.title("Temperature Trend")

plt.subplot(1, 2, 2)
plt.bar(monthly_rain.index, monthly_rain.values)
plt.title("Monthly Rainfall")

plt.tight_layout()
plt.savefig("combined_plot.png")
plt.show()


monthly_stats = df.groupby('month').agg({
    'temperature': ['mean', 'max', 'min'],
    'rainfall': 'sum',
    'humidity': 'mean'
})

print("\nMONTHLY STATISTICS:")
print(monthly_stats)


df.to_csv("cleaned_weather_data.csv", index=False)

with open("summary.txt", "w") as f:
    f.write(str(monthly_stats))
