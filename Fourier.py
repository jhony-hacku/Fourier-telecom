import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def texto_a_binario(texto):
    return ''.join(format(ord(c), '08b') for c in texto)  # Convertir texto a binario en una sola cadena

# Solicitar entrada al usuario
entrada = input("Ingresa una letra o palabra (case sensitive): ")
resultado = texto_a_binario(entrada)

print(f"Texto: {entrada}")
print(f"Binario: {resultado}")

# --------------------- Configuración de la señal ---------------------
T_val = 1                    # Periodo normalizado
num_bits = len(resultado)     # Longitud de la señal en bits
bit_sequence = [int(b) for b in resultado]  # Convertir la cadena binaria en lista de enteros
interval_length = T_val / num_bits  # Duración de cada bit

# --------------------- Discretización de la señal g(t) ---------------------
num_samples = 1000
t_values = np.linspace(0, T_val, num_samples)
g_values = np.array([bit_sequence[min(int(t // interval_length), num_bits-1)] for t in t_values], dtype=float)

# --------------------- Cálculo NUMÉRICO de coeficientes de Fourier ---------------------
num_harmonics = int(input("Ingrese el número de armónicos: "))

a_n_values = []
b_n_values = []

for n in range(1, num_harmonics + 1):
    a_n = (2 / T_val) * np.trapz(g_values * np.sin(2 * np.pi * n * t_values), t_values)
    b_n = (2 / T_val) * np.trapz(g_values * np.cos(2 * np.pi * n * t_values), t_values)
    a_n_values.append(a_n)
    b_n_values.append(b_n)

# Coeficiente c (componente DC)
c = (1 / T_val) * np.trapz(g_values, t_values)

# Magnitud del espectro
magnitude_spectrum = np.sqrt(np.array(a_n_values) ** 2 + np.array(b_n_values) ** 2)

# --------------------- Gráfica del espectro ---------------------
frequencies = np.arange(1, num_harmonics + 1)
plt.figure(figsize=(10, 4))
plt.stem(frequencies, magnitude_spectrum, basefmt=" ")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud")
plt.title(f"Espectro de Frecuencias de la señal '{resultado}'")
plt.grid(True)
plt.show()

# --------------------- Reconstrucción de la serie de Fourier ---------------------
t_eval = np.linspace(0, T_val, num_samples)
fourier_series = c * np.ones_like(t_eval)

for n in range(1, num_harmonics + 1):
    fourier_series += a_n_values[n - 1] * np.sin(2 * np.pi * n * t_eval) + b_n_values[n - 1] * np.cos(2 * np.pi * n * t_eval)

# --------------------- Gráfica de la reconstrucción ---------------------
plt.figure(figsize=(10, 4))
plt.plot(t_values, g_values, label="Señal original", linestyle='--')
plt.plot(t_eval, fourier_series, label=f"Reconstrucción con {num_harmonics} armónicos", color='red')
plt.xlabel("Tiempo (t)")
plt.ylabel("Amplitud")
plt.legend()
plt.grid(True)
plt.title("Comparación señal original vs reconstrucción")
plt.show()

# --------------------- Tabla de coeficientes ---------------------
df_coeficientes = pd.DataFrame({
    "n": np.arange(1, num_harmonics + 1),
    "a_n": a_n_values,
    "b_n": b_n_values,
    "Magnitud": magnitude_spectrum
})

print("\nCoeficientes calculados:")
print(df_coeficientes.to_string(index=False))
