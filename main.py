import tkinter as tk
from tkinter import ttk
import random
from PIL import Image, ImageTk
import DEFmodulo as mod
from colorama import init, Fore, Style
import time

init()

for i in range(21):
    bar = "⋆" * i + "-" * (20 - i)
    print(Fore.BLUE + f"[{bar}] {i*5}%" + Style.RESET_ALL, end="\r")
    time.sleep(0.1)

print("\n" + Fore.GREEN + "Cargado!" + Style.RESET_ALL)

ventana = tk.Tk()
ventana.title("Chiikawa Shop")
ventana.geometry("796x556")

fondos = (
    "C:/Users/celia/OneDrive/Desktop/CACHIWATI/imageneschiikawa/chiikawa1.jpg",
    "C:/Users/celia/OneDrive/Desktop/CACHIWATI/imageneschiikawa/chiikawa2.jpg",
    "C:/Users/celia/OneDrive/Desktop/CACHIWATI/imageneschiikawa/chiikawa3.jpg",
    "C:/Users/celia/OneDrive/Desktop/CACHIWATI/imageneschiikawa/chiikawa4.jpg",
    "C:/Users/celia/OneDrive/Desktop/CACHIWATI/imageneschiikawa/chiikawa5.jpg",
    "C:/Users/celia/OneDrive/Desktop/CACHIWATI/imageneschiikawa/chiikawa6.jpg"
)
randomfondo = random.choice(fondos)

RUTA_FONDO = randomfondo

try:
    imagen_pil = Image.open(RUTA_FONDO).resize((796, 556), Image.Resampling.LANCZOS)
    imagen_tk = ImageTk.PhotoImage(imagen_pil)

    label_fondo = tk.Label(ventana, image=imagen_tk)
    label_fondo.place(x=0, y=0, relwidth=1, relheight=1)
except:
    print(Fore.RED + "No se encontraron las imagenes!, cargando fondo simple...")
    ventana.configure(bg="lemon chiffon")

tk.Label(
    ventana,
    text="✮ Chiikawa Shop ✮",
    font=("Arial", 20, "bold"),
    bg="white",
    relief="solid",
    padx=5,
    pady=5
).pack(pady=20)

ttk.Button(ventana, text="Registrar venta", width=30, command=mod.ventana_registrar).pack(pady=5)
ttk.Button(ventana, text="Mostrar ventas", width=30, command=mod.ventana_mostrar).pack(pady=5)
ttk.Button(ventana, text="Calcular total de ventas", width=30, command=mod.ventana_total).pack(pady=5)
ttk.Button(ventana, text="Mostrar gráfica de ventas", width=30, command=mod.ventana_grafica).pack(pady=5)
ttk.Button(ventana, text="Eliminar una venta", width=30, command=mod.ventana_eliminar).pack(pady=5)
ttk.Button(ventana, text="Salir", width=30, command=ventana.quit).pack(pady=20)

ventana.mainloop()
