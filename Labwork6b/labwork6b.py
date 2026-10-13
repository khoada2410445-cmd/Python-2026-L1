import os
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
scores_csv_path = os.path.join(BASE_DIR, 'scores.csv')

df = pd.read_csv(scores_csv_path)
df.columns = df.columns.str.lower()
courses = ['math', 'python', 'db']

# 1. Scatter plot -> scattered.png
plt.figure(figsize=(8, 6))
for course in courses:
    if course in df.columns:
        plt.scatter(df.index, df[course], label=course.capitalize(), alpha=0.7, s=50)

plt.title('Student Scores Scatter Plot', fontsize=14)
plt.xlabel('Student Index', fontsize=12)
plt.ylabel('Score', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.savefig(os.path.join(BASE_DIR, 'scattered.png'), bbox_inches='tight')
plt.close()

# 2. Histograms (3 subplots) -> histo.png
fig, axes = plt.subplots(1, 3, figsize=(15, 5), sharey=True)
for i, course in enumerate(courses):
    if course in df.columns:
        axes[i].hist(df[course], bins=8, color='skyblue', edgecolor='black', alpha=0.7)
        axes[i].set_title(f'{course.capitalize()} Marks')
        axes[i].set_xlabel('Score')
        axes[i].set_ylabel('Frequency')
        axes[i].grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig(os.path.join(BASE_DIR, 'histo.png'), bbox_inches='tight')
plt.close()

# 3. Box plot -> box.png 
plt.figure(figsize=(8, 6))
data_to_plot = [df[c] for c in courses if c in df.columns]
labels = [c.capitalize() for c in courses if c in df.columns]

plt.boxplot(data_to_plot, tick_labels=labels, patch_artist=True,
            boxprops=dict(facecolor='lightgreen', color='green'))

plt.title('Box Plot of Course Marks', fontsize=14)
plt.ylabel('Score', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)
plt.savefig(os.path.join(BASE_DIR, 'box.png'), bbox_inches='tight')
plt.close()

print("[Labwork 6b] All plots generated successfully!")