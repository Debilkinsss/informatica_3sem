import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('flights.csv')
stats = df.groupby('CARGO').agg(flights_count=('PRICE', 'count'), total_price=('PRICE', 'sum'), total_weight=('WEIGHT', 'sum')).reset_index()
print("Статистика по авиакомпаниям:")
print(stats)
fig, axes = plt.subplots(1, 3, figsize=(13, 6))

#Графики графики графики
axes[0].bar(stats['CARGO'], stats['flights_count'])
axes[0].set_title('Количество рейсов')
axes[0].set_ylabel('Рейсы')

axes[1].bar(stats['CARGO'], stats['total_price'])
axes[1].set_title('Общая стоимость')
axes[1].set_ylabel('Стоимость')

axes[2].bar(stats['CARGO'], stats['total_weight'])
axes[2].set_title('Общий вес')
axes[2].set_ylabel('Вес')

plt.tight_layout()
plt.show()