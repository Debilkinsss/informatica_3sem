import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

data = np.loadtxt('data.txt')
N = len(data)

A = np.eye(N)  #создаем матрицу единичную размером NxN
for i in range(N):
    A[i, (i - 1) % N] = -1.0  #-1 добавляем как в примере на lms
history = [data.copy()]

for n in range(255):
    data = 0.5 * data + 0.5 * np.roll(data, 1) #сдвиг массива вправо и взятие среднего
    history.append(data.copy())

history = np.array(history)
fig, ax = plt.subplots(figsize=(10, 6))

def animate(frame):
    ax.clear()
    ax.plot(history[frame], 'b-', linewidth=2)
    ax.set_ylim(np.min(history) - 0.5, np.max(history) + 0.5)
    ax.set_xlim(0, N - 1)
    ax.set_title(f'Шаг времени: {frame}/255')
    ax.set_xlabel('Позиция x')
    ax.set_ylabel('data(x)')
    ax.grid(True, alpha=0.3)

    ax.set_xticks([0, 10, 20, 30, 40, 50])
    ax.set_yticks([0, 2, 4, 6, 8, 10])

#ура гифка
anim = FuncAnimation(fig, animate, frames=256, interval=50, repeat=True)
plt.show()

#результат в статике
plt.figure(figsize=(10, 6))
plt.plot(history[0], 'b-', alpha=0.5, label='Начальное (n=0)')
plt.plot(history[-1], 'r-', linewidth=2, label='Финальное (n=255)')
plt.ylim(np.min(history) - 0.5, np.max(history) + 0.5)
plt.xlim(0, N - 1)
plt.xticks([0, 10, 20, 30, 40, 50])
plt.yticks([0, 2, 4, 6, 8, 10])
plt.title('Изменение за 255 шагов')
plt.xlabel('Позиция x')
plt.ylabel('data(x)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()