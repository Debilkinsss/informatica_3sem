import matplotlib.pyplot as plt
x = []
y = []
files = ['001.dat', '002.dat', '003.dat', '004.dat', '005.dat']
for name in files:
    with open(name, 'r') as f:
        n = f.readline()
        for _ in range(int(n)):
            a = f.readline().split()
            x.append(float(a[0]))
            y.append(float(a[1]))
        plt.figure(figsize=(10, 5))
        plt.scatter(x, y)
        plt.show()
        x = []
        y = []
