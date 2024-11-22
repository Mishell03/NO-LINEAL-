import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Función para graficar
def plot_function(f, x, title, second_derivative=None):
    y = f(x)
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label="f(x)", linewidth=2)
    if second_derivative is not None:
        y2 = second_derivative(x)
        plt.plot(x, y2, '--', label="f''(x)", linewidth=1.5)
    plt.axhline(0, color="black", linewidth=0.8, linestyle="--")
    plt.axvline(0, color="black", linewidth=0.8, linestyle="--")
    plt.title(title)
    plt.legend()
    plt.grid()
    st.pyplot(plt)

st.title("Análisis de Convexidad y Concavidad de Funciones")

# Ejercicio 1
st.subheader("1. Demuestre que la función f(x) = 3x + 2 es convexa en R")
f1 = lambda x: 3 * x + 2
x = np.linspace(-10, 10, 400)
plot_function(f1, x, "f(x) = 3x + 2")
st.write("f''(x) = 0. Como es no negativa, la función es convexa en R.")

# Ejercicio 2
st.subheader("2. Verifique si f(x) = x³ es convexa, cóncava o ninguna en [0,∞)")
f2 = lambda x: x**3
f2_derivative_2 = lambda x: 6 * x  # Segunda derivada
x = np.linspace(0, 10, 400)
plot_function(f2, x, "f(x) = x³ y su segunda derivada", f2_derivative_2)
st.write("En [0, ∞), la segunda derivada f''(x) = 6x ≥ 0, por lo que es convexa en este intervalo.")

# Ejercicio 3
st.subheader("3. Demuestre que f(x) = e²ˣ es convexa en R")
f3 = lambda x: np.exp(2 * x)
f3_derivative_2 = lambda x: 4 * np.exp(2 * x)  # Segunda derivada
x = np.linspace(-2, 2, 400)
plot_function(f3, x, "f(x) = e²ˣ y su segunda derivada", f3_derivative_2)
st.write("f''(x) = 4e²ˣ > 0 para todo x, por lo que la función es convexa en R.")

# Ejercicio 4
st.subheader("4. Análisis de la función f(x) = ln(x)")
f4 = lambda x: np.log(x)
f4_derivative_2 = lambda x: -1 / x**2  # Segunda derivada
x = np.linspace(0.1, 10, 400)
plot_function(f4, x, "f(x) = ln(x) y su segunda derivada", f4_derivative_2)
st.write("En (0, ∞), f''(x) = -1/x² ≤ 0, por lo que f(x) es cóncava en su dominio.")

# Ejercicio 5
st.subheader("5. Análisis de f(x) = x⁴ - 2x² + 1")
f5 = lambda x: x*4 - 2 * x*2 + 1
f5_derivative_2 = lambda x: 12 * x**2 - 4  # Segunda derivada
x = np.linspace(-2, 2, 400)
plot_function(f5, x, "f(x) = x⁴ - 2x² + 1 y su segunda derivada", f5_derivative_2)
st.write("""
1. La función es convexa donde f''(x) ≥ 0, es decir, en (-∞, -√(1/3)] ∪ [√(1/3), ∞).
2. La función es cóncava donde f''(x) < 0, es decir, en (-√(1/3), √(1/3)).
3. Puntos de inflexión: x = ±√(1/3).
""")