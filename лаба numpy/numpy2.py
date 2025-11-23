import numpy as np
import matplotlib.pyplot as plt

def filter(data):
    f_data = np.zeros_like(data)
    for i in range(len(data)):
        delta = data[max(0, i - 9):i + 1]
        f_data[i] = np.mean(delta)
    return f_data


files = ['signal01.dat', 'signal02.dat', 'signal03.dat']
for file in files:
    data = np.loadtxt(file)
    f_data = filter(data)

    plt.subplot(2, 1, 1)
    plt.plot(data, 'b-', alpha=0.7, linewidth=1)
    plt.title(f'Исходный сигнал')
    plt.ylabel('Значение')
    plt.grid(True, alpha=0.3)

    plt.subplot(2, 1, 2)
    plt.plot(f_data, 'r-', linewidth=1.5)
    plt.title(f'Отфильтрованный сигнал')
    plt.ylabel('Значение')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()