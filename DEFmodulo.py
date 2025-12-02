#librerías
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk, messagebox
import os
from PIL import Image, ImageTk
import random
from playsound3 import playsound

#diccionario de productos
chiikawas = [
    {"id": 1, "nombre": "Chiikawa", "precio": 287.92},
    {"id": 2, "nombre": "Hachiware", "precio": 287.92},
    {"id": 3, "nombre": "Usagi", "precio": 287.92},
    {"id": 4, "nombre": "Kuri Manju", "precio": 287.92},
    {"id": 5, "nombre": "Rakko", "precio": 287.92},
    {"id": 6, "nombre": "Momonga", "precio": 287.92}
]

#archivo para lista de compras
archivo = "ventas.txt"


def cargar_df():
    if not os.path.exists(archivo) or os.path.getsize(archivo) == 0:
        return pd.DataFrame(columns=["nombre", "precio"])
    return pd.read_csv(archivo, header=None, names=["nombre", "precio"])

def guardar_df(df):
    df.to_csv(archivo, index=False, header=False)

def ventana_registrar():
    win = tk.Toplevel()
    win.title("Registrar Venta")
    win.geometry("350x250")
    win.configure(bg="khaki")

    tk.Label(win, text="Selecciona un producto:", font=("Arial", 12), bg="khaki").pack(pady=10)

    opciones = [c["nombre"] for c in chiikawas]
    seleccion = tk.StringVar(value=opciones[0])

    ttk.OptionMenu(win, seleccion, opciones[0], *opciones).pack(pady=5)

    def registrar():
        nombre = seleccion.get()
        precio = next(c["precio"] for c in chiikawas if c["nombre"] == nombre)
        
        df = cargar_df()
        df.loc[len(df)] = [nombre, precio]
        guardar_df(df)

        messagebox.showinfo("Venta Registrada", f"✔ Venta: {nombre}")
        win.destroy()

        if nombre == "Usagi":
            playsound("C:/Users/celia/OneDrive/Desktop/CACHIWATI/audio/Usagi.mp3")
        elif nombre == "Hachiware":
            playsound("C:/Users/celia/OneDrive/Desktop/CACHIWATI/audio/Hachiware.mp3")
        elif nombre == "Chiikawa":
            playsound("C:/Users/celia/OneDrive/Desktop/CACHIWATI/audio/Chiikawa.mp3")
        elif nombre == "Momonga":
            playsound("C:/Users/celia/OneDrive/Desktop/CACHIWATI/audio/Momonga.mp3")
        elif nombre == "Kuri Manju":
            playsound("C:/Users/celia/OneDrive/Desktop/CACHIWATI/audio/Kurimanju.mp3")
        elif nombre == "Rakko":
            playsound("C:/Users/celia/OneDrive/Desktop/CACHIWATI/audio/rakko.mp3")
        else:
            print("nowe")

    ttk.Button(win, text="Registrar", command=registrar).pack(pady=20)


def ventana_mostrar():
    df = cargar_df()
    if df.empty:
        messagebox.showwarning("Sin ventas", "No hay ventas registradas.")
        return

    tabla = df.groupby("nombre").agg(
        cantidad=("nombre", "count"),
        precio_unit=("precio", "mean"),
        total=("precio", "sum")
    )

    win = tk.Toplevel()
    win.title("Lista de Ventas")
    win.geometry("400x350")
    win.configure(bg="peach puff")

    txt = tk.Text(win, width=50, height=15)
    txt.pack(pady=10)

    txt.insert(tk.END, "✦ Lista de Ventas Agrupadas ✦\n\n")
    txt.insert(tk.END, tabla.to_string())
    txt.config(state="disabled")

def ventana_total():
    df = cargar_df()

    if df.empty:
        messagebox.showwarning("Sin ventas", "No hay ventas registradas.")
        return

    subtotal = df["precio"].sum()
    descuento = subtotal * 0.10 if subtotal > 1000 else 0
    total = subtotal - descuento

    messagebox.showinfo("Total de Ventas",
                        f"Subtotal: ${subtotal:.2f}\n"
                        f"Descuento: ${descuento:.2f}\n"
                        f"Total: ${total:.2f}")

def ventana_grafica():
#lista 
    df = cargar_df()
    if df.empty:
        messagebox.showwarning("Sin ventas", "No hay ventas para graficar.")
        return

    tabla = df.groupby("nombre")["precio"].sum()

    win = tk.Toplevel()
    win.title("Gráfica de Ventas")
    win.geometry("600x400")

    figura = plt.Figure(figsize=(6, 4))
    ax = figura.add_subplot(111)

    ax.pie(
        tabla.values,
        labels=tabla.index,
        autopct='%1.1f%%',
        startangle=90,
        colors=['mistyrose', 'steelblue', 'palegreen', 'mediumpurple', 'khaki', 'cornsilk' ]
    )
    ax.set_title("Ventas por Producto")

    canvas = FigureCanvasTkAgg(figura, master=win)
    canvas.draw()
    canvas.get_tk_widget().pack()

def ventana_eliminar():
    df = cargar_df()
    if df.empty:
        messagebox.showwarning("Sin ventas", "No hay ventas registradas.")
        return

    win = tk.Toplevel()
    win.title("Eliminar Venta")
    win.geometry("400x300")
    win.configure(bg="cornflower blue")

    tk.Label(win, text="Selecciona una venta a eliminar:", font=("Arial", 12), bg="cornflower blue").pack(pady=10)

    lista = tk.Listbox(win, width=50, height=10)
    lista.pack()

    for i, row in df.iterrows():
        lista.insert(tk.END, f"{i+1}. {row['nombre']} — ${row['precio']}")

    def eliminar():
        seleccion = lista.curselection()
        if not seleccion:
            return messagebox.showerror("Error", "Debes seleccionar una venta.")

        index = seleccion[0]
        df2 = df.drop(df.index[index])
        guardar_df(df2)

        messagebox.showinfo("Eliminado", "Venta eliminada correctamente.")
        win.destroy()

    ttk.Button(win, text="Eliminar", command=eliminar).pack(pady=15)