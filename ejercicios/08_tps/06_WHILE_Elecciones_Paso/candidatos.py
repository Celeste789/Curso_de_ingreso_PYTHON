'''
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por consola (print)

'''
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        nombre_candidatos = []
        edades_candidatos = []
        votos_candidatos = []
        cantidad_votos_total = 0
        suma_edades_candidatos = 0
        mayor_cantidad_votos = None
        menor_cantidad_votos = None
        indice_votos_maximo = 0
        indice_votos_minimo = 0
        flag = True

        while flag:
            nombre_candidato_particular = prompt(title="Nombre", prompt="Ingrese el nombre del candidato")
            edad_candidato_particular_txt = prompt(title="Edad", prompt="Ingrese la edad del candidato")
            votos_candidato_particular_txt = prompt(title="Cantidad de votos", prompt="Ingrese cantidad de votos")
            
            if nombre_candidato_particular != None and edad_candidato_particular_txt != None and votos_candidato_particular_txt != None:
                nombre_candidatos.append(nombre_candidato_particular)
                edad_candidato_particular = int(edad_candidato_particular_txt)
                while edad_candidato_particular < 25 and flag:
                    edad_candidato_particular_txt = prompt(title="Edad", prompt="Ingrese la edad del candidato")
                    if edad_candidato_particular_txt == None:
                        flag = False
                edades_candidatos.append(edad_candidato_particular)
                votos_candidato_particular = int(votos_candidato_particular_txt)
                while votos_candidato_particular < 0 and flag:
                    votos_candidato_particular_txt = prompt(title="Cantidad de votos", prompt="Ingrese cantidad de votos")
                    if votos_candidato_particular_txt == None:
                        flag = False
                votos_candidatos.append(votos_candidato_particular)
            
            else:
                flag = False
            
            for i in range(0, len(votos_candidatos)):
                if menor_cantidad_votos != None and votos_candidatos[i] < menor_cantidad_votos:
                    indice_votos_minimo = i
                else:
                    mayor_cantidad_votos = votos_candidatos[0]
                if mayor_cantidad_votos != None and votos_candidatos[i] > mayor_cantidad_votos:
                    indice_votos_maximo = i
                else:
                    menor_cantidad_votos = votos_candidatos[0]
                suma_edades_candidatos += edades_candidatos[i]
                cantidad_votos_total += votos_candidatos[i]

        nombre_candidato_mayor_votos = nombre_candidatos[indice_votos_maximo]
        nombre_candidato_menor_votos = nombre_candidatos[indice_votos_minimo]
        edad_candidato_menos_votos = edades_candidatos[indice_votos_minimo]
        promedio_edades = suma_edades_candidatos / len(edades_candidatos)

        mensaje = f"El candidato con mas votos es {nombre_candidato_mayor_votos}"
        mensaje2 = f"El candidato con menos votos es {nombre_candidato_menor_votos} y su edad es {edad_candidato_menos_votos}"
        mensaje3 = f"El promedio de edades de los candidatos es de {promedio_edades}"
        mensaje4 = f"El total de votos emitidos es {cantidad_votos_total}"
        mensaje_final = f"{mensaje}\n{mensaje2}\n{mensaje3}\n{mensaje4}"

        print(mensaje_final)






if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
