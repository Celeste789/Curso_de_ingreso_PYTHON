import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Maria Celeste
Gonzalez Pereira

Al presionar el botón Mostrar pedir un número. mostrar los números divisores desde el 1 al número ingresado, 
y mostrar la cantidad de números divisores encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        numero_a_dividir_txt = prompt(title="", prompt="Ingrese el numero a calcular")
        cantidad_divisores = 0
        if numero_a_dividir_txt != None:
            numero_a_dividir = int(numero_a_dividir_txt)
            for i in range(1, numero_a_dividir):
                if numero_a_dividir % i == 0:
                    alert(title="Divisor", message= str(i))
                    cantidad_divisores += 1
            alert(title="Cantidad de divisores", message=f"La cantidad de divisores es {cantidad_divisores}")
                

        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()