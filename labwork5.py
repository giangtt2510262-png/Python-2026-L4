import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load datasets from CSV files
students_df = pd.read_csv('students (1).csv')
scores_df = pd.read_csv('scores (1).csv')

# 2. Handle missing values (Data Cleaning)
students_cleaned = students_df.copy()
students_cleaned['age'] = students_cleaned['age'].fillna(students_cleaned['age'].median())
students_cleaned['GPA'] = students_cleaned['GPA'].fillna(students_cleaned['GPA'].mean())

scores_cleaned = scores_df.copy()
scores_cleaned['math'] = scores_cleaned['math'].fillna(scores_cleaned['math'].mean())
scores_cleaned['database'] = scores_cleaned['database'].fillna(scores_cleaned['database'].mean())

# 3. Merge datasets and calculate overall average score
df = pd.merge(students_cleaned, scores_cleaned, on='student_id')
df['average_score'] = df[['python', 'math', 'database']].mean(axis=1)

# 4. Set up visual theme and subplot layout
sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# --- Plot 1: Average GPA by Major ---
avg_gpa = df.groupby('major')['GPA'].mean().reset_index()
sns.barplot(data=avg_gpa, x='major', y='GPA', ax=axes[0, 0], palette='Blues_d')
axes[0, 0].set_title('Average GPA by Major', fontsize=12, fontweight='bold')
axes[0, 0].set_ylim(0, 4.0)

for p in axes[0, 0].patches:
    axes[0, 0].annotate(f"{p.get_height():.2f}", 
                        (p.get_x() + p.get_width() / 2., p.get_height()),
                        ha='center', va='center', xytext=(0, 5), textcoords='offset points')

# --- Plot 2: Average Test Score by Major ---
avg_score = df.groupby('major')['average_score'].mean().reset_index()
sns.barplot(data=avg_score, x='major', y='average_score', ax=axes[0, 1], palette='Greens_d')
axes[0, 1].set_title('Average Test Score by Major', fontsize=12, fontweight='bold')
axes[0, 1].set_ylim(0, 100)

for p in axes[0, 1].patches:
    axes[0, 1].annotate(f"{p.get_height():.2f}", 
                        (p.get_x() + p.get_width() / 2., p.get_height()),
                        ha='center', va='center', xytext=(0, 5), textcoords='offset points')

# --- Plot 3: Top 5 Students by Average Score ---
top5 = df.sort_values(by='average_score', ascending=False).head(5)
sns.barplot(data=top5, x='name', y='average_score', ax=axes[1, 0], palette='Purples_d')
axes[1, 0].set_title('Top 5 Students by Average Score', fontsize=12, fontweight='bold')
axes[1, 0].set_ylim(0, 100)

for p in axes[1, 0].patches:
    axes[1, 0].annotate(f"{p.get_height():.2f}", 
                        (p.get_x() + p.get_width() / 2., p.get_height()),
                        ha='center', va='center', xytext=(0, 5), textcoords='offset points')

# --- Plot 4: Correlation between GPA and Average Test Score ---
sns.scatterplot(data=df, x='GPA', y='average_score', hue='major', style='major', s=100, ax=axes[1, 1])
axes[1, 1].set_title('GPA vs. Average Test Score', fontsize=12, fontweight='bold')

# Adjust layout, save figure, and display
plt.tight_layout()
plt.savefig('labwork5_visualization.png', dpi=300)
plt.show()
