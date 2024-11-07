import tkinter as tk
from tkinter import messagebox



class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Ventana Principal")
        self.root.geometry("300x200")


        self.close_button = tk.Button(self.root, text="Cerrar ventana", command=self.on_close)
        self.close_button.pack(pady=20)


    def on_close(self):
        response = messagebox.askquestion("Confirmar Cierre", "¿Estás seguro de que quieres cerrar la ventana?")
        if response == "yes":
            self.root.quit()
        else:
            pass



class CustomWindow(MainWindow):
    def __init__(self, root):
        super().__init__(root)
        self.root.title("Ventana Personalizada")


    def on_close(self):
        response = messagebox.askyesno("Confirmar Cierre", "¿Estás seguro de que deseas cerrar la ventana?")
        if response:
            self.root.quit()
        else:
            pass


if __name__ == "__main__":
    root = tk.Tk()


    app = CustomWindow(root)


    root.protocol("WM_DELETE_WINDOW", app.on_close)
    root.mainloop()
