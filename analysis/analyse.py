import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# fetch data from your Django API
data = requests.get('http://127.0.0.1:8000/api/entries/').json()
df = pd.DataFrame(data)

print("Your learning data:")
print(df)
print("\nTotal minutes per language:")
print(df.groupby('language')['minutes'].sum())

# create a bar chart
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x='language', y='minutes', palette='viridis')
plt.title('Study Time by Language')
plt.xlabel('Language')
plt.ylabel('Minutes')
plt.tight_layout()
plt.savefig('analysis/study_time.png')
print("\nChart saved to analysis/study_time.png")