import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import tkinter as tk
import math as mt

'''
La juguetería El MUNDO DE OCTAVIO nos encarga un programa para conocer qué cantidad de materiales se necesita para la fabricación de distintos juguetes.

COMETA: 

AB = Diámetro mayor (se debe calcular)
DC = diámetro menor (se ingresa por prompt)
BD y BC = lados menores (se ingresa por prompt)
AD y AC = lados mayores (se ingresa por prompt)

Debemos tener en cuenta que la estructura del cometa estará dada por un perímetro de varillas de plástico y los correspondientes entrecruces (DC y AB) del mismo material para mantener la forma del cometa.
El cometa estará construido con papel de alta resistencia.
La cola del mismo se construirá con el mismo papel que el cuerpo y representará un 10% adicional del necesario para el cuerpo.
Necesitamos saber cuántos Mts de varillas de plástico y cuántos de papel son necesarios para la construcción en masa de 10 cometas. Tener en cuenta que los valores de entrada están expresados en Cms.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text="El Cometa", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
        
        self.label_diametro_menor = customtkinter.CTkLabel(master=self, text="Diametro Menor DC")
        self.label_diametro_menor.grid(row=1, column=0, padx=20, pady=10)

        self.txt_diametro_menor= customtkinter.CTkEntry(master=self)
        self.txt_diametro_menor.grid(row=1, column=1)
        
        self.label_lados_menores = customtkinter.CTkLabel(master=self, text="Lados Menores BD y BC")
        self.label_lados_menores.grid(row=2, column=0, padx=20, pady=10)

        self.txt_lados_menores = customtkinter.CTkEntry(master=self)
        self.txt_lados_menores.grid(row=2, column=1)

        self.label_lados_mayores = customtkinter.CTkLabel(master=self, text="Lados Mayores AD y AC")
        self.label_lados_mayores.grid(row=3, column=0, padx=20, pady=10)

        self.txt_lados_mayores = customtkinter.CTkEntry(master=self)
        self.txt_lados_mayores.grid(row=3, column=1)
                
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=4, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        diametro_menor_texto = self.txt_diametro_menor.get()
        diametro_menor_numero = float(diametro_menor_texto)
        lado_menor_texto = self.txt_lados_menores.get()
        lado_menor = float(lado_menor_texto)
        lado_mayor_texto = self.txt_lados_mayores.get()
        lado_mayor = float(lado_mayor_texto) 
        diametro_menor_numero_mitad = (diametro_menor_numero / 2)**2
        cuadrado_lado_menor = lado_menor ** 2
        cuadrado_lado_mayor = lado_mayor ** 2

        diametro_mayor_corto = mt.sqrt(cuadrado_lado_menor - diametro_menor_numero_mitad)
        diametro_mayor_largo = mt.sqrt(cuadrado_lado_mayor - diametro_menor_numero_mitad)
        diametro_mayor = diametro_mayor_largo + diametro_mayor_corto

        varillas_por_cometa = (lado_mayor + lado_menor) * 2 + diametro_mayor + diametro_menor_numero
        area_cometa = diametro_mayor * diametro_menor_numero / 2
        area_cometa_y_cola_ms = area_cometa * 1.1 / 100
        varillas_por_cometa_ms = varillas_por_cometa / 100

        area_cometa_total = area_cometa_y_cola_ms * 10
        varillas_cometa_total = varillas_por_cometa_ms * 10

        mensaje = f"El area por cometa es {area_cometa_y_cola_ms} \n El area por 10 cometas es {area_cometa_total} \n El total de varillas para una cometa es {varillas_por_cometa_ms} \n El total de varillas por 10 cometas es {varillas_cometa_total}"

        alert(title="", message=mensaje)





    
if __name__ == "__main__":
    app = App()
    app.mainloop()