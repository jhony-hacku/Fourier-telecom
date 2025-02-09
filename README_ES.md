# 📡 Análisis de Fourier en Redes y Telecomunicaciones

## 📖 Descripción
Este proyecto implementa **Análisis de Fourier** para la representación de señales en el contexto de **redes y telecomunicaciones**, basado en el libro *Redes de Computadoras - Tanenbaum (5ta Edición)*. A través de la **descomposición en series de Fourier**, analizamos cómo se pueden modelar señales periódicas y calcular su **espectro de frecuencias**, lo que es fundamental para la transmisión de datos en distintos medios, como:
- **Cables de cobre y fibra óptica** (medios guiados)
- **Radiofrecuencia y satélites** (medios inalámbricos)
- **Telefonía y transmisión digital**

## 🎯 Objetivo
- Representar **señales digitales** en el dominio del tiempo usando series de Fourier.
- Calcular y graficar el **espectro de frecuencias** de una señal dada.
- Ilustrar la importancia de los **armónicos de Fourier** en la reconstrucción de señales.

## 🛠 Características del Programa
- Implementación en **Python** con **SymPy** y **Matplotlib**.
- Cálculo de coeficientes de Fourier \( a_n \) , \( b_n \) y \( c \). 
- Representación de señales en el **dominio del tiempo**.
- Cálculo y graficación del **espectro de frecuencias**.

## 📌 Conceptos Claves
✔ **Transformada de Fourier** 📊  
✔ **Espectro de Frecuencias** 📶  
✔ **Armónicos y Señales Digitales** 🔀  

## 📌 Conceptos Claves
✔ **Transformada de Fourier** 📊  
✔ **Espectro de Frecuencias** 📶  
✔ **Armónicos y Señales Digitales** 🔀  

## ⚙️ Cómo funciona
Este programa utiliza la **Serie de Fourier** para analizar y representar señales en redes y telecomunicaciones. A continuación, se describen los pasos principales:

1. **Definición de coeficientes de Fourier**  
   - Se calculan los coeficientes \( a_n \) y \( b_n \) a partir de la señal de entrada.
   - Se usa SymPy para realizar las operaciones simbólicas.

2. **Cálculo de la Serie de Fourier**  
   - Se genera la sumatoria de términos senoidales y cosenoidales hasta un número \( N \) de armónicos.
   - Esto permite aproximar señales periódicas con un conjunto finito de frecuencias.

3. **Evaluación en el dominio del tiempo**  
   - Se evalúa la función en distintos valores de \( t \) para reconstruir la señal en el tiempo.
   - Se representa gráficamente la señal original y su aproximación con Fourier.

4. **Cálculo del espectro de frecuencias**  
   - Se obtiene la magnitud \( M_n \) de los coeficientes de Fourier, que indica la energía en cada frecuencia.
   - Se grafica el espectro, mostrando cómo cada armónico contribuye a la señal.

Este proceso permite visualizar cómo **las redes y los sistemas de telecomunicaciones transmiten señales digitales y analógicas**, y cómo el **ancho de banda limita la transmisión de datos**.


---

🚀
