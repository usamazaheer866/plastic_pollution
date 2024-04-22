#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("global-plastics-production.csv")

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(df.head())

# Data Cleaning
# Check for missing values
print("\nChecking for missing values:")
print(df.isnull().sum())

# Data Visualization
# Plotting global plastics production over the years
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='Year', y='Global plastics production (million tonnes)', marker='o')
plt.title("Global Plastics Production Over Time")
plt.xlabel("Year")
plt.ylabel("Plastics Production (million tonnes)")
plt.grid(True)
plt.show()

# Statistical Summary
print("\nStatistical Summary of Global Plastics Production:")
print(df.describe())


# In[ ]:




