import tkinter as tk
from tkinter import messagebox


class InfoPopup:
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def mostrar_info(self):
        messagebox.showinfo("Información", self.mensaje)


class ErrorPopup:
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def mostrar_error(self):
        messagebox.showerror("Error", self.mensaje)


class CustomPopup(InfoPopup, ErrorPopup):
    def __init__(self, mensaje_info, mensaje_error):
        InfoPopup.__init__(self, mensaje_info)
        ErrorPopup.__init__(self, mensaje_error)

    def mostrar_mensajes(self):
        self.mostrar_info()
        self.mostrar_error()


popup = CustomPopup("Este es un mensaje informativo.", "¡Oops! Hubo un error.")


popup.mostrar_mensajes()


tk.Tk().withdraw()
