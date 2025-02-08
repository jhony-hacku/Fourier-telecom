import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Definir variables simbólicas
n = sp.symbols('n', integer=True)
t = sp.symbols('t', real=True)

# Definir los coeficientes de Fourier
a_n_expr = (1 / (sp.pi * n)) * (-sp.cos(sp.pi * n / 2) + sp.cos(sp.pi * n / 4) - sp.cos(7 * sp.pi * n/4) + sp.cos(sp.pi * n))
b_n_expr = (1 / (sp.pi * n)) * (sp.sin(sp.pi * n / 2) - sp.sin(sp.pi * n / 4) + sp.sin(7 * sp.pi * n/4) - sp.sin(sp.pi * n))

# Definir la magnitud M_n
M_n_expr = sp.sqrt(a_n_expr**2 + b_n_expr**2)

# Definir la sumatoria de Fourier y evaluarla con doit()
max_n = 40  # Número de términos en la sumatoria
sum_expr = sp.Sum(b_n_expr * sp.cos(2 * sp.pi * n * t) + a_n_expr * sp.sin(2 * sp.pi * n * t), (n, 1, max_n)).doit()

# ----- Cálculo de los coeficientes M_n -----
n_values = [0]  # Incluir n=0
M_n_values = [1]  # M_0 = 1

for i in range(1, max_n + 1):
    M_n_val = float(sp.N(M_n_expr.subs(n, i)))  # Convertir a flotante
    n_values.append(i)
    M_n_values.append(M_n_val)

# ----- Evaluación de la serie de Fourier -----
t_values = np.arange(0, 1.01, 0.01)
sum_values = []  # Lista para guardar los valores de la sumatoria

for t_val in t_values:
    evaluated_expr = sum_expr.subs(t, t_val)  # Sustituir t por el valor actual
    final = 1/2 + evaluated_expr  # Sumar 1/2
    sum_values.append(float(final.evalf()))  # Convertir a número decimal y agregar a la lista

# Mostrar resultados individuales para max_n = 40
print("\nValores individuales:")
print(f"{'n':<5} {'a_n':<20} {'b_n':<20} {'M_n':<20}")
print("="*65)

for i in range(len(n_values)):  
    print(f"{n_values[i]:<5} {float(sp.N(a_n_expr.subs(n, n_values[i]))):<20.6f} {float(sp.N(b_n_expr.subs(n, n_values[i]))):<20.6f} {M_n_values[i]:<20.6f}")


print("\n")

# ----- Graficar los coeficientes M_n (sin líneas, solo puntos) -----
plt.figure(figsize=(8, 5))
plt.plot(n_values, M_n_values, marker='o', linestyle='', color='r', label=r"$M_n = \sqrt{a_n^2 + b_n^2}$")  # Sin línea
plt.xlabel("n (Índice de la serie de Fourier)")
plt.ylabel(r"$M_n$")
plt.title("Coeficientes de la Serie de Fourier")
plt.legend()
plt.grid(True)
plt.show()

# ----- Graficar la serie de Fourier -----
plt.figure(figsize=(8, 5))
plt.plot(t_values, sum_values, label="Serie de Fourier", color='b', linewidth=2)
plt.xlabel("t")
plt.ylabel("Valor de la sumatoria")
plt.title("Aproximación de la Serie de Fourier")
plt.legend()
plt.grid()
plt.show()