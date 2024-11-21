import pandas as pd
import numpy as np

# Task 1: 

df = pd.read_csv('Instagram-Data.csv')

missing_values = df.isnull().sum()
print("missing values in every coluamn:\n", missing_values)

numeric_cols = df.select_dtypes(include=[np.number]).columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

categorical_cols = df.select_dtypes(include=['object']).columns
df = df.dropna(subset=categorical_cols)

# Task 2:
 
print("Columns in df:\n", df.columns)
try:
  pivot_followers_by_category = df.pivot_table(values='Followers', index='Category', aggfunc='mean')
except Exception as e:
  print("there is error", e)
  
print("\npivot table followers by category:\n", pivot_followers_by_category)

try:
  pivot_engagement_by_country_category = df.pivot_table(values='Authentic engagement', index=['Audience Country', 'Category'], aggfunc='max')
except Exception as e:
  print("there is error:", e)
  
print("\npivot table by max authentic engagement by country and category:\n", pivot_engagement_by_country_category)

top_10_influencers = df.nlargest(10, 'Authentic engagement')['Account']  
print("\ntop 10 influencerss by maximum authentic engagement:\n", top_10_influencers)

engagement_mean = df['Engagement avg'].mean() 
filtered_influencers = df[(df['Rank'] < 20) & (df['Engagement avg'] > engagement_mean)]['Account']  
print("\nfiltered influencers by rank and engagement avg:\n", filtered_influencers)
