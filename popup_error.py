import tkinter as tk
from tkinter import messagebox


class ErrorPopup:
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def mostrar_error(self):
        messagebox.showerror("Error", self.mensaje)


class CustomErrorPopup(ErrorPopup):
    def __init__(self, mensaje):
        super().__init__(mensaje)

    def mostrar_error(self):

        messagebox.showerror("¡Error!", f"¡Ups! Ocurrió un problema:\n{self.mensaje}")


popup = CustomErrorPopup("Este es un mensaje de error.")


popup.mostrar_error()


tk.Tk().withdraw()
