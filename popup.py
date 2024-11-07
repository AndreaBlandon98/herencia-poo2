import tkinter as tk
from tkinter import messagebox



class PopupBase:
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def mostrar_mensaje(self):
        messagebox.showinfo("Información", self.mensaje)



class CustomPopup(PopupBase):
    def __init__(self, mensaje):
        super().__init__(mensaje)

    def mostrar_mensaje(self):
        messagebox.showinfo("Mensaje Personalizado", f"¡Nuevo mensaje!\n{self.mensaje}")



ventana = CustomPopup("Este es el mensaje de ejemplo")


ventana.mostrar_mensaje()


tk.Tk().withdraw()
