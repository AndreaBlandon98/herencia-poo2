import tkinter as tk
from tkinter import messagebox


class InfoPopup:
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def mostrar_mensaje(self):
        messagebox.showinfo("Información", self.mensaje)


class WarningPopup:
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def mostrar_mensaje(self):
        messagebox.showwarning("Advertencia", self.mensaje)


class CombinedPopup(InfoPopup, WarningPopup):
    def __init__(self, mensaje_info, mensaje_warning):

        InfoPopup.__init__(self, mensaje_info)
        WarningPopup.__init__(self, mensaje_warning)

    def mostrar_mensajes(self):

        InfoPopup.mostrar_mensaje(self)

        WarningPopup.mostrar_mensaje(self)


popup = CombinedPopup("Este es un mensaje informativo.", "¡Cuidado! Esto es una advertencia.")


popup.mostrar_mensajes()


tk.Tk().withdraw()
