import numpy as np
import matplotlib.pyplot as plt
from scipy import linalg

def solve_and_plot(filename):
    with open(filename, 'r') as f:
        n = int(f.readline().strip())
        A = [list(map(float, f.readline().strip().split())) for _ in range(n)]
        b = list(map(float, f.readline().strip().split()))

    A, b = np.array(A), np.array(b)
    x = linalg.solve(A, b)

    plt.figure(figsize=(12, 6))
    plt.bar(range(len(x)), x, color='skyblue')
    plt.xlabel('Индекс i')
    plt.ylabel('x[i]')
    plt.title(f'Решение системы уравнений (n={n})')
    plt.xticks(range(0, len(x), max(1, len(x) // 20)))  #подписи каждые 5% индексов
    plt.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    plt.show()


solve_and_plot('real_data.txt')