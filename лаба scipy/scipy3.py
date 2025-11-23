import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
def dy_dx(x, y):
    return -2 * y

x = sp.Symbol('x')
y = sp.Function('y')

diff_yx = sp.Eq(y(x).diff(x), -2*y(x))
initial_condition= {y(0): sp.sqrt(2)}

s_sol = sp.dsolve(diff_yx, y(x), ics=initial_condition)
y_sym = s_sol.rhs #символьное решение
print(y_sym)

#далее - численное решение
y0 = [np.sqrt(2)]
n_sol = solve_ivp(dy_dx, (0,10), y0, t_eval=np.linspace(0, 10, 1000))
x_values = np.linspace(0, 10, 1000)
y_symbolic_values = np.array([y_sym.subs(x, x_val) for x_val in x_values], dtype=float)
y_numerical_values = n_sol.y[0]
difference = y_symbolic_values - y_numerical_values

plt.figure(figsize=(15, 5))

plt.subplot(1, 2, 1)
plt.plot(x_values, y_symbolic_values, 'b-', linewidth=2, label='SymPy')
plt.plot(n_sol.t, n_sol.y[0], 'r--', linewidth=1.5, label='SciPy')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.title('Решения: dy/dx = -2y, y(0) = √2')
plt.legend()
plt.grid(True, alpha=0.3)

plt.subplot(1, 2, 2)
plt.plot(x_values, difference, 'g-', linewidth=1.5)
plt.xlabel('x')
plt.ylabel('Разность (SymPy - SciPy)')
plt.title('Разность решений')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()