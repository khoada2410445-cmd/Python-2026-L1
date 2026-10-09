import os
import pandas as pd

# Automatically locate files relative to this script's directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STUDENTS_CSV = os.path.join(BASE_DIR, 'students.csv')
SCORES_CSV = os.path.join(BASE_DIR, 'scores.csv')

# ==========================================
# PART 1: DATA MANIPULATION ON STUDENTS.CSV
# ==========================================
print("=== PART 1: Data Manipulation (students.csv) ===")

# 1. Load the dataset
df_students = pd.read_csv(STUDENTS_CSV)
print("\n[1] Dataset loaded successfully.")

# 2. Display first five rows
print("\n[2] First 5 rows of students dataset:")
print(df_students.head())

# 3. Find number of rows and columns
num_rows, num_cols = df_students.shape
print(f"\n[3] Shape of dataset: {num_rows} rows and {num_cols} columns")

# 4. Select name and GPA
name_col = [c for c in df_students.columns if 'name' in c.lower()][0]
gpa_col = [c for c in df_students.columns if 'gpa' in c.lower()][0]

print("\n[4] Selecting Name and GPA:")
print(df_students[[name_col, gpa_col]])

# 5. Find students with GPA >= 3.5
print("\n[5] Students with GPA >= 3.5:")
high_gpa = df_students[df_students[gpa_col] >= 3.5]
print(high_gpa)

# 6. Sort students by GPA
print("\n[6] Students sorted by GPA (descending):")
sorted_students = df_students.sort_values(by=gpa_col, ascending=False)
print(sorted_students)

# 7. Find average GPA by major
major_col = [c for c in df_students.columns if 'major' in c.lower()][0]
print("\n[7] Average GPA by Major:")
avg_gpa_major = df_students.groupby(major_col)[gpa_col].mean()
print(avg_gpa_major)


# ==========================================
# PART 2: MERGING AND ANALYZING DATASETS
# ==========================================
print("\n" + "=" * 50)
print("=== PART 2: Working with students.csv & scores.csv ===")

# 1. Load both files
df_students = pd.read_csv(STUDENTS_CSV)
df_scores = pd.read_csv(SCORES_CSV)
print("\n[1] Both datasets loaded.")

# 2. Check missing values
print("\n[2] Checking missing values...")
print("Missing values in students.csv:")
print(df_students.isnull().sum())
print("\nMissing values in scores.csv:")
print(df_scores.isnull().sum())

# 3. Handle missing data appropriately
df_students_clean = df_students.dropna().copy()
df_scores_clean = df_scores.dropna().copy()
print("\n[3] Cleaned missing data.")

# 4. Merge the two datasets
id_student = [c for c in df_students_clean.columns if 'id' in c.lower()][0]
id_score = [c for c in df_scores_clean.columns if 'id' in c.lower()][0]

merged_df = pd.merge(df_students_clean, df_scores_clean, left_on=id_student, right_on=id_score)
print("\n[4] Merged Dataset (first 5 rows):")
print(merged_df.head())

# 5. Calculate each student's average score
numeric_score_cols = [c for c in df_scores_clean.select_dtypes(include=['float64', 'int64']).columns if 'id' not in c.lower()]

if numeric_score_cols:
    merged_df['Average_Score'] = merged_df[numeric_score_cols].mean(axis=1)
else:
    score_col = [c for c in merged_df.columns if any(k in c.lower() for k in ['score', 'gpa', 'mark'])][0]
    merged_df['Average_Score'] = merged_df[score_col]

name_col_merged = [c for c in merged_df.columns if 'name' in c.lower()][0]
print("\n[5] Students Average Scores:")
print(merged_df[[id_student, name_col_merged, 'Average_Score']])

# 6. Find the top 5 students
print("\n[6] Top 5 Students:")
top_5_students = merged_df.sort_values(by='Average_Score', ascending=False).head(5)
print(top_5_students[[id_student, name_col_merged, 'Average_Score']])

# 7. Compute average score by major
major_col_merged = [c for c in merged_df.columns if 'major' in c.lower()][0]
print("\n[7] Average Score by Major:")
avg_score_major = merged_df.groupby(major_col_merged)['Average_Score'].mean()
print(avg_score_major)