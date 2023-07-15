
'''
Nombre: Maria Celeste
Apellido: Gonzalez Pereira
'''

import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import tkinter as tk


class App(customtkinter.CTk):
   
    def __init__(self):
        super().__init__()


        self.title("UTN FRA")
        self.minsize(320, 250)


        self.label_title = customtkinter.CTkLabel(master=self, text="Tour", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=4, pady=20, columnspan=2, sticky="nsew")
   
    def btn_mostrar_on_click(self):
        #Datos personales
        
        nombre = prompt(title="Nombre", prompt="Ingrese su nombre")
        edad_txt = prompt(title="Edad", prompt="Ingrese su edad")
        genero = prompt(title="Genero", prompt="Ingrese su genero")
        altura_txt = prompt(title="Altura", prompt="Ingrese su altura")
        while nombre == None or len(nombre) < 3 or nombre.isdigit():
            nombre = prompt(title="Nombre", prompt="Ingrese un nombre correcto")
        while edad_txt == None or not(edad_txt.isdigit()):
            edad_txt = prompt(title="Edad", prompt="Ingrese una edad correcta")
        while genero == None or (genero != "F" and genero != "M" and genero != "Other"):
            genero = prompt(title="Genero", prompt="Ingrese un genero correcto")
        while altura_txt == None or not(altura_txt.isdigit()):
            altura_txt = prompt(title="Altura", prompt="Ingrese una altura correcta")
        edad = int(edad_txt) #parsear
        altura = int(altura_txt)
        if altura < 140:
            mensaje_altura = "baja"
        elif altura < 170:
            mensaje_altura = "media"
        elif altura < 190:
            mensaje_altura = "alta"
        else:
            mensaje_altura = "muy alta"
        mensaje = f"Usted es  {nombre} tiene {edad} años de edad y su género es {genero} y su altura es {mensaje_altura}"
        alert(title="", message=mensaje)
        

        #Excursiones

        cantidad_excursiones_caminando = 0
        cantidad_excursiones_vehiculo = 0
        precio_total_excursiones = 0
        precio_mas_alto = None
        precio_mas_bajo = None
        cantidad_excursiones_txt = prompt(title="Cantidad de excursiones", prompt="Ingrese la cantidad de excursiones")
        while cantidad_excursiones_txt == None or not(cantidad_excursiones_txt.isdigit()):
            cantidad_excursiones_txt = prompt(title="Cantidad de excursiones", prompt="Ingrese la cantidad de excursiones")
        cantidad_excursiones = int(cantidad_excursiones_txt)
        contador_excursiones = 0
        while contador_excursiones < cantidad_excursiones:
            precio_txt = prompt(title="Precio", prompt="Ingrese el precio")
            while precio_txt == None or not(precio_txt.isdigit()):
                precio_txt = prompt(title="Precio", prompt="Ingrese el precio")
            precio = int(precio_txt)
            transporte = prompt(title="Medio de transporte", prompt="Ingrese el medio de transporte")
            while transporte == None or (transporte != "Caminata" and transporte != "Vehiculo"):
                transporte = prompt(title="Medio de transporte", prompt="Ingrese el medio de transporte")
            if precio_mas_bajo == None or precio_mas_bajo > precio:
                precio_mas_bajo = precio
            if precio_mas_alto == None or precio_mas_alto < precio:
                precio_mas_alto = precio
            precio_total_excursiones += precio  
            if transporte == "Caminta":
                cantidad_excursiones_caminando += 1
            else:
                cantidad_excursiones_vehiculo += 1
            contador_excursiones += 1
        precio_promedio = precio_total_excursiones / cantidad_excursiones
        if cantidad_excursiones_caminando > cantidad_excursiones_vehiculo:
            mensaje_tipo_excursion = "Fueron mas excursiones caminando"
        elif cantidad_excursiones_caminando < cantidad_excursiones_vehiculo:
            mensaje_tipo_excursion = "Fueron mas excursiones en vehiculo"
        else:
            mensaje_tipo_excursion = "Hubo misma cantidad de excursiones caminando que en vehiculo"
        mensaje1 = f"El precio mas alto es {precio_mas_alto} \n El precio mas bajo es {precio_mas_bajo} \n El precio promedio es {precio_promedio}"
        alert(title = "Precios", message = mensaje1)
        alert(title = "Tipo excursion", message = mensaje_tipo_excursion)



if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
