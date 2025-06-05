import math
import cmath
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import messagebox

def determinante(x1, y1, x2, y2):
    return (x1 * y2) - (x2 * y1)

def form_gen(a, b, c):
    p = (b ** 2)
    resultado = p - 4 * a * c
    return (-b + cmath.sqrt(resultado)) / (2 * a)

def plot_phase_portrait(a1, b1, a2, b2):
    x = np.linspace(-2, 2, 20)
    y = np.linspace(-2, 2, 20)
    X, Y = np.meshgrid(x, y)
    dx = a1 * X + b1 * Y
    dy = a2 * X + b2 * Y

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.quiver(X, Y, dx, dy, color='blue', scale=20)
    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('y', fontsize=12)
    ax.axhline(0, color='black', lw=1, ls='--')
    ax.axvline(0, color='black', lw=1, ls='--')
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.grid(color='gray', linestyle='--', linewidth=0.5)
    ax.set_aspect('equal')

    return fig

def calculate_equations(a1, b1, a2, b2):
    try:
        deter = determinante(a1, b1, a2, b2)
        suma = a1 + b2

        if deter == 0:
            messagebox.showerror("Error", "ERROR: El punto crítico (0,0) de la ecuación no es único")
            return

        # Polinomio característico
        l1 = form_gen(1, suma, deter)
        l2 = form_gen(1, suma, deter)

        # Clasificación
        if isinstance(l1, complex) and isinstance(l2, complex):
            au = l1.real
            ad = l2.real
            b = l1.imag

            if au > 0 and ad > 0:
                tipo = "Repulsor"
                espiral = "no espiral" if b == 0 else "espiral"
            elif au < 0 and ad < 0:
                tipo = "Atractor"
                espiral = "no espiral" if b == 0 else "espiral"
            elif au == 0 and ad == 0:
                tipo = "Línea de puntos" if b == 0 else "Centro"
            elif au > 0 and ad < 0:
                tipo = "Silla"
            else:
                tipo = "Inestable"

            message = f"El punto crítico (0,0) es un {tipo} {espiral}." if 'espiral' in locals() else f"El punto crítico (0,0) es una {tipo}."
            messagebox.showinfo("Resultado", message)

        else:
            if (l1 > 0 and l2 > 0) or (l1 < 0 and l2 < 0):
                tipo = "Nodo"
                estabilidad = "estable" if suma == 0 else "inestable"
                messagebox.showinfo("Resultado", f"El punto crítico (0,0) es un {tipo} {estabilidad}.")
            else:
                messagebox.showinfo("Resultado", "El punto crítico (0,0) es una silla inestable.")

        # Graficar
        fig = plot_phase_portrait(a1, b1, a2, b2)
        return fig

    except Exception as e:
        messagebox.showerror("Error", str(e))

def on_calculate():
    a1 = int(a1_entry.get())
    b1 = int(b1_entry.get())
    a2 = int(a2_entry.get())
    b2 = int(b2_entry.get())
    
    fig = calculate_equations(a1, b1, a2, b2)
    if fig:
        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.grid(row=5, columnspan=4)
        canvas.draw()

# Configurar ventana principal
window = tk.Tk()
window.title("Análisis de Puntos Críticos")

# Entradas de parámetros
tk.Label(window, text="a1:").grid(row=0, column=0)
a1_entry = tk.Entry(window)
a1_entry.grid(row=0, column=1)
a1_entry.insert(0, "1")

tk.Label(window, text="b1:").grid(row=1, column=0)
b1_entry = tk.Entry(window)
b1_entry.grid(row=1, column=1)
b1_entry.insert(0, "1")

tk.Label(window, text="a2:").grid(row=2, column=0)
a2_entry = tk.Entry(window)
a2_entry.grid(row=2, column=1)
a2_entry.insert(0, "1")

tk.Label(window, text="b2:").grid(row=3, column=0)
b2_entry = tk.Entry(window)
b2_entry.grid(row=3, column=1)
b2_entry.insert(0, "1")

# Botón para calcular
calculate_button = tk.Button(window, text="Calcular", command=on_calculate)
calculate_button.grid(row=4, columnspan=2)

# Ejecutar el bucle principal de la ventana
window.mainloop()
