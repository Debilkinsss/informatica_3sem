import matplotlib.pyplot as plt
with open('2.txt', 'r') as f:
    x1 = [float(a) for a in f.readline().split()]
    y1 = [float(a) for a in f.readline().split()]
    x2 = [float(a) for a in f.readline().split()]
    y2 = [float(a) for a in f.readline().split()]
    x3 = [float(a) for a in f.readline().split()]
    y3 = [float(a) for a in f.readline().split()]
    x4 = [float(a) for a in f.readline().split()]
    y4 = [float(a) for a in f.readline().split()]
    x5 = [float(a) for a in f.readline().split()]
    y5 = [float(a) for a in f.readline().split()]
    x6 = [float(a) for a in f.readline().split()]
    y6 = [float(a) for a in f.readline().split()]
all_x = x1 + x2 + x3 + x4 + x5 + x6 #определяем пределы общие
all_y = y1 + y2 + y3 + y4 + y5 + y6
x_min = min(all_x)
x_max = max(all_x)
y_min = min(all_y)
y_max = max(all_y)
dx = (x_max - x_min) * 0.05 #отступы для лучшей читаемости
dy = (y_max - y_min) * 0.05
x_lim = [x_min - dx, x_max + dx]
y_lim = [y_min - dy, y_max + dy]

plt.figure(figsize=(12, 8))

plt.subplot(2, 3, 1)
plt.plot(x1, y1)
plt.xlim(x_lim)
plt.ylim(y_lim)
plt.grid(True)
plt.title('Frame 1')

plt.subplot(2, 3, 2)
plt.plot(x2, y2)
plt.xlim(x_lim)
plt.ylim(y_lim)
plt.grid(True)
plt.title('Frame 2')

plt.subplot(2, 3, 3)
plt.plot(x3, y3)
plt.xlim(x_lim)
plt.ylim(y_lim)
plt.grid(True)
plt.title('Frame 3')

plt.subplot(2, 3, 4)
plt.plot(x4, y4)
plt.xlim(x_lim)
plt.ylim(y_lim)
plt.grid(True)
plt.title('Frame 4')

plt.subplot(2, 3, 5)
plt.plot(x5, y5)
plt.xlim(x_lim)
plt.ylim(y_lim)
plt.grid(True)
plt.title('Frame 5')

plt.subplot(2, 3, 6)
plt.plot(x6, y6)
plt.xlim(x_lim)
plt.ylim(y_lim)
plt.grid(True)
plt.title('Frame 6')

plt.tight_layout()
plt.show()