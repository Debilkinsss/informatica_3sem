import sympy as sp

lambd, mu, ro = sp.symbols('lambda mu ro', real=True, positive=True)

A = sp.Matrix([
    [0, 0, 0, -1/ro, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, -1/ro, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, -1/ro, 0, 0, 0],
    [-(lambd + 2*mu), 0, 0, 0, 0, 0, 0, 0, 0],
    [0, -mu, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, -mu, 0, 0, 0, 0, 0, 0],
    [-lambd, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [-lambd, 0, 0, 0, 0, 0, 0, 0, 0]
])

eigenvals_dict = A.eigenvals() #получим собственные значения

items_list = list(eigenvals_dict.items())
counter = 0
i = 1
while counter < len(items_list):
    val, mult = items_list[counter]
    sim = sp.simplify(val)
    print("λ" + str(i) + " (кратность " + str(mult) + "): " + str(sim))
    counter += 1
    i += 1