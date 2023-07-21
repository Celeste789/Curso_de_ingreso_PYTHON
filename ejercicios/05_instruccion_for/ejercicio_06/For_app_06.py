import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Al presionar el botón Mostrar pedir un número. mostrar los números pares desde 
el 1 al número ingresado, y mostrar la cantidad de números pares encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        cantidad_repeticiones_txt = prompt(title="", prompt="Ingrese la cantidad de repeticiones")
        cantidad_pares_encontrados = 0
        if cantidad_repeticiones_txt != None:
            cantidad_repeticiones = int(cantidad_repeticiones_txt)
            for i in range(1, cantidad_repeticiones):
                if i % 2 == 0:
                    alert(title="", message=i)
                    cantidad_pares_encontrados += 1
        alert(title="", message=f"cantidad de pares encontrados {cantidad_pares_encontrados}")


        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()