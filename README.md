# 📡 Fourier Analysis in Networking and Telecommunications

## 📖 Description
This project implements **Fourier Analysis** for signal representation in the context of **networking and telecommunications**, based on the book *Computer Networks - Tanenbaum (5th Edition)*. Through **Fourier series decomposition**, we analyze how periodic signals can be modeled and calculate their **frequency spectrum**, which is fundamental for data transmission in various media, such as:
- **Copper cables and fiber optics** (guided media)
- **Radiofrequency and satellites** (wireless media)
- **Telephony and digital transmission**

## 🎯 Objective
- Represent **digital signals** in the time domain using Fourier series.
- Calculate and plot the **frequency spectrum** of a given signal.
- Illustrate the importance of **Fourier harmonics** in signal reconstruction.

## 🛠 Program Features
- Implementation in **Python** using **SymPy** and **Matplotlib**.
- Calculation of Fourier coefficients \( a_n \), \( b_n \), and \( c \).
- Representation of signals in the **time domain**.
- Calculation and visualization of the **frequency spectrum**.

## 📌 Key Concepts
✔ **Fourier Transform** 📊  
✔ **Frequency Spectrum** 📶  
✔ **Harmonics and Digital Signals** 🔀  

## ⚙️ How It Works
This program utilizes the **Fourier Series** to analyze and represent signals in networking and telecommunications. The main steps are as follows:

1. **Definition of Fourier Coefficients**  
   - The coefficients \( a_n \) and \( b_n \) are calculated from the input signal.
   - SymPy is used for symbolic operations.

2. **Calculation of the Fourier Series**  
   - A summation of sine and cosine terms up to a number \( N \) of harmonics is generated.
   - This allows for the approximation of periodic signals with a finite set of frequencies.

3. **Evaluation in the Time Domain**  
   - The function is evaluated at different \( t \) values to reconstruct the signal over time.
   - The original signal and its Fourier approximation are graphically represented.

4. **Computation of the Frequency Spectrum**  
   - The magnitude \( M_n \) of the Fourier coefficients is obtained, indicating the energy at each frequency.
   - The spectrum is plotted, showing how each harmonic contributes to the signal.

This process enables visualization of how **networking and telecommunications systems transmit digital and analog signals** and how **bandwidth limitations affect data transmission**.

---

🚀

