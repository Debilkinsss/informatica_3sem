import matplotlib.pyplot as plt
data = []
with open('students.csv', 'r', encoding='utf-8') as f:
    for line in f:
        parts = line.strip().split(';')
        prep = parts[0].strip()
        group = parts[1].strip()
        mark = int(parts[2].strip())
        data.append((prep, group, mark))

prep_stats = {}
for prep, group, mark in data:
    if prep not in prep_stats:
        prep_stats[prep] = {}
    prep_stats[prep][mark] = prep_stats[prep].get(mark, 0) + 1
group_stats = {}
for prep, group, mark in data:
    if group not in group_stats:
        group_stats[group] = {}
    group_stats[group][mark] = group_stats[group].get(mark, 0) + 1
preps = sorted(prep_stats.keys())
groups = sorted(group_stats.keys())
marks = sorted(set(mark for _, _, mark in data))

prep_data = []
for prep in preps:
    row = []
    for mark in marks:
        row.append(prep_stats[prep].get(mark, 0))
    prep_data.append(row)
group_data = []
for group in groups:
    row = []
    for mark in marks:
        row.append(group_stats[group].get(mark, 0))
    group_data.append(row)

plt.figure(figsize=(14, 6))
plt.subplot(1, 2, 1)
bottom = [0] * len(preps)
for i in range(len(marks)):
    values = []
    for j in range(len(preps)):
        values.append(prep_data[j][i])
    plt.bar(preps, values, bottom=bottom)
    for j in range(len(preps)):
        bottom[j] += values[j]
plt.title('Marks per prep')
plt.ylabel('Count')
plt.subplot(1, 2, 2)
bottom = [0] * len(groups)
for i in range(len(marks)):
    values = []
    for j in range(len(groups)):
        values.append(group_data[j][i])
    plt.bar(groups, values, bottom=bottom, label=str(marks[i]))
    for j in range(len(groups)):
        bottom[j] += values[j]
plt.title('Marks per group')
plt.ylabel('Count')
plt.legend()
plt.tight_layout()
plt.show()