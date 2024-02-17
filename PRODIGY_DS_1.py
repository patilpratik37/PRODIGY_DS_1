# Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Loading the data
df=pd.read_csv("G:/Pratik Profile PC/Desktop/PRODIGY INFOTECH INTERNSHIP TASKS/TASK_01/world_population.csv")

#Top 5 values of our dataset
df.head()

#Shape of our dataset
df.shape

#Information about our dataset
df.info()

#Missing values
df.isnull().sum()

#Grouping data
continent_df= df.groupby(by='Continent').sum()
continent_df
continent_df['2022 Population'].plot(kind='pie', figsize=(10,5), shadow=True, autopct='%1.1f%%')
plt.title(' Population Distribution by Continent')
plt.axis('equal')
plt.show()

# Creating dataframes for countries per continent

# Asia
asian_countries= df.loc[df["Continent"]=="Asia"].sort_values(by=["2022 Population"], ascending=False, ignore_index=True)

# Africa
african_countries= df.loc[df["Continent"]=="Africa"].sort_values(by=["2022 Population"], ascending=False, ignore_index=True)

# Europe
european_countries= df.loc[df["Continent"]=="Europe"].sort_values(by=["2022 Population"], ascending=False, ignore_index=True)

# North America
na_countries= df.loc[df["Continent"]=="North America"].sort_values(by=["2022 Population"], ascending=False, ignore_index=True)

# Oceania
oc_countries= df.loc[df["Continent"]=="Oceania"].sort_values(by=["2022 Population"], ascending=False, ignore_index=True)

# South America
sa_countries= df.loc[df["Continent"]=="South America"].sort_values(by=["2022 Population"], ascending=False, ignore_index=True)

# Plotting top 5 most populated countries by continent

# Asian countries
top_5_countries= asian_countries[["Country/Territory", "2022 Population"]].sort_values(by="2022 Population", ascending=False).head(5)
sns.barplot(data=top_5_countries, x="Country/Territory", y="2022 Population")
plt.xlabel("Country/Territory")
plt.ylabel("2022 Population")
plt.title("Top 5 Countries by Population in Asian Countries")
plt.show()

# African
top_5_african= african_countries[["Country/Territory", "2022 Population"]].sort_values(by= "2022 Population", ascending=False).head(5)
sns.barplot(data=top_5_african, x= "Country/Territory", y= "2022 Population")
plt.xlabel("Country/Territory")
plt.ylabel("2022 Population")
plt.title("Top 5 Countries by Population in African Countries")

# European
top_5_european= european_countries [["Country/Territory", "2022 Population"]].sort_values(by= "2022 Population", ascending=False).head(5)
sns.barplot(data= top_5_european, x= "Country/Territory", y= "2022 Population")
plt.xlabel("Country/Territory")
plt.ylabel("2022 Population")
plt.title("Top 5 Countries by Population in europ Countries")

# North America
top_5_na= na_countries [["Country/Territory", "2022 Population"]].sort_values(by= "2022 Population", ascending=False).head(5)
sns.barplot(data= top_5_na, x="Country/Territory", y="2022 Population")
plt.xlabel("Country/Territory")
plt.ylabel("2022 Population")
plt.title("Top 5 Countries by Population in North America Countries")

# Oceania
top_5_oc= oc_countries [["Country/Territory", "2022 Population"]].sort_values(by= "2022 Population", ascending=False).head(5)
sns.barplot(data= top_5_oc, x= "Country/Territory", y= "2022 Population")
plt.xlabel("Country/Territory")
plt.ylabel("2022 Population")
plt.title("Top 5 Countries by Population in Oceania Countries")

# South America
top_5_sa= sa_countries [["Country/Territory", "2022 Population"]].sort_values(by= "2022 Population", ascending=False).head(5)
sns.barplot(data=top_5_sa, x= "Country/Territory", y= "2022 Population")
plt.xlabel("Country/Territory")
plt.ylabel("2022 Population")
plt.title("Top 5 Countries by Population in South America Countries")

# World population trend
plt.subplots(figsize=(10,5))
trend= df.iloc[:,5:13].sum().sort_values(ascending=True)
sns.lineplot(x=trend.index, y=trend.values, marker="o")
plt.xticks(rotation=20)
plt.ylabel("Population")
plt.title("World Population Trend (1970-2022)")
plt.show()