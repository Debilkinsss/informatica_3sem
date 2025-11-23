import pandas as pd
import matplotlib.pyplot as plt

students = pd.read_excel('students_info.xlsx', sheet_name='logins')
students = students.dropna(subset=['login'])

faculty_stats = students.groupby('group_faculty').agg({'login': 'count', 'group_out': lambda x: list(x.unique())}).reset_index()
faculty_stats.columns = ['group_faculty', 'student_count', 'out_groups']

print("Факультетские группы успешных студентов:")
for _, row in faculty_stats.iterrows():
    groups_out = [int(x) for x in row['out_groups']]  # Преобразуем в обычные числа
    print(f"Группа {row['group_faculty']}: {row['student_count']} студентов")
    print(f"Группы по информатике: {sorted(groups_out)}")
    print()

out_stats = students.groupby('group_out').agg({'login': 'count','group_faculty': lambda x: list(x.unique())}).reset_index()
out_stats.columns = ['group_out', 'student_count', 'faculty_groups']

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
students['group_faculty'].value_counts().sort_index().plot(kind='bar', color='skyblue')
plt.title('Студенты по факультетским группам')
plt.xlabel('Факультетская группа')
plt.ylabel('Количество')

plt.subplot(1, 2, 2)
students['group_out'].value_counts().sort_index().plot(kind='bar', color='lightcoral')
plt.title('Студенты по группам информатики')
plt.xlabel('Группа по информатике')
plt.ylabel('Количество')

plt.tight_layout()
plt.show()