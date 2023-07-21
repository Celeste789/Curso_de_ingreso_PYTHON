'''
Maria Celeste
Gonzalez Pereira

De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
e. se pide ingresar el sexo (M , F , NB) , informar cuantos candidatos hay de cada sexo
f. se pide ingresar nivel de aceptacion de imagen del candidato (entre -100 y 100) informar el
nombre y sexo del que mejor nivel tiene 
g.de las personas de sexo femenino ,informar cuanta hay mayores a 50 y cuantas menores a esa edad
h. de que sexo hubo mas candidatos
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
        cantidad_mayor_votos = None
        cantidad_menor_votos = None
        nombre_candidato_mayor_votos = None
        edad_candidato_menor_votos = None
        contador_de_candidatos = 0
        suma_edades = 0
        suma_total_votos = 0
        cantidad_canditos_f = 0
        cantidad_canditos_m = 0
        cantidad_canditos_nb = 0
        nombre_candidato_mayor_aceptacion = None
        genero_candidato_mayor_aceptacion = None
        nivel_aceptacion_mayor = None
        mujeres_mayores_50 = 0
        mujeres_menores_50 = 0

        flag = True
        while flag:
            nombre_candidato = None
            edad_candidato_txt = None
            cantidad_votos_candidato_txt = None
            genero_candidato = None
            nivel_aceptacion_candidato_txt = None

            while nombre_candidato == None or nombre_candidato == "" or not nombre_candidato.isalpha():
                nombre_candidato = prompt(title="Edad", prompt="Ingrese nomnbre candidato")
            
            while edad_candidato_txt == None or int(edad_candidato_txt) < 25 or not edad_candidato_txt.isdigit():
                edad_candidato_txt = prompt(title="Nombre", prompt="Ingrese la edad")
            edad_candidato = int(edad_candidato_txt)
            suma_edades += edad_candidato
            contador_de_candidatos += 1

            while cantidad_votos_candidato_txt == None or int(cantidad_votos_candidato_txt) < 0 or not cantidad_votos_candidato_txt.isdigit():
                cantidad_votos_candidato_txt = prompt(title= "Cantidad de votos", prompt="Ingrese la cantidad de votos")
            cantidad_votos_candidato = int(cantidad_votos_candidato_txt)

            #e. Ingresar el sexo (M , F , NB) , informar cuantos candidatos hay de cada sexo
            #g. De las personas de sexo femenino ,informar cuanta hay mayores a 50 y cuantas menores a esa edad
            while genero_candidato != "F" and genero_candidato != "M" and genero_candidato != "NB":
                genero_candidato = prompt(title="Genero del candidato", prompt="Ingrese el genero del candidato")
                match genero_candidato:
                    case "F":
                        cantidad_canditos_f += 1
                        if edad_candidato <= 50:
                            mujeres_menores_50 += 1
                        else:
                            mujeres_mayores_50 += 1
                    case "M":
                        cantidad_canditos_m +=1
                    case _:
                        cantidad_canditos_nb += 1
            
            #f. Se pide ingresar nivel de aceptacion de imagen del candidato (entre -100 y 100) informar el nommbre y sexo del que mejor nivel tiene 
            while nivel_aceptacion_candidato_txt == None or int(nivel_aceptacion_candidato_txt) < -100 or int(nivel_aceptacion_candidato_txt) > 100:
                nivel_aceptacion_candidato_txt = prompt(title="Nivel de aceptacion", prompt="Ingrese el nivel de aceptacion")
            nivel_aceptacion_candidato = int(nivel_aceptacion_candidato_txt)

            cancelar = question(title="Cancelar", message="Desea cancelar?")
            if cancelar:
                flag = False

            #a. Nombre del candidato con mas votos       
            
            if cantidad_mayor_votos == None or cantidad_mayor_votos < cantidad_votos_candidato:
                cantidad_mayor_votos = cantidad_votos_candidato
                #tenes que cambiar la cantidad de votos tambien
                nombre_candidato_mayor_votos = nombre_candidato
            
            #b. Nombre y edad del candidato con menos votos

            if cantidad_menor_votos == None or cantidad_menor_votos > cantidad_votos_candidato:
                cantidad_menor_votos = cantidad_votos_candidato
                #tenes que cambiar la cantidad de votos tambien
                nombre_candidato_menor_votos = nombre_candidato
                edad_candidato_menor_votos = edad_candidato

            #d. Suma total de votos

            suma_total_votos += cantidad_votos_candidato

            #f.
            if nivel_aceptacion_mayor == None or nivel_aceptacion_candidato > nivel_aceptacion_mayor:
                nivel_aceptacion_mayor = nivel_aceptacion_candidato
                nombre_candidato_mayor_aceptacion = nombre_candidato
                genero_candidato_mayor_aceptacion = genero_candidato


        #c. Promedio de edades de los candidatos

        promedio_edades = suma_edades / contador_de_candidatos

        #h. De que sexo hubo mas candidatos
        if cantidad_canditos_f < cantidad_canditos_m and cantidad_canditos_m > cantidad_canditos_nb:
            genero_mayor_candidatos = "M"
        elif cantidad_canditos_f > cantidad_canditos_nb:
            genero_mayor_candidatos = "F"
        else:
            genero_mayor_candidatos = "NB"         

        mensaje_candidato_mayor_votos = f"El nombre del candidato con mayor votos es {nombre_candidato_mayor_votos}"
        mensaje_candidato_menor_votos = f"El nombre del candidato con menos votos es {nombre_candidato_menor_votos} y su edad es {edad_candidato_menor_votos}"
        mensaje_promedio_edades = f"El promedio de edades de los candidatos es {promedio_edades}"
        mensaje_cantidad_votos_total = f"La cantidad total de votos es {suma_total_votos}"
        mensaje_cantidad_candidatos_f = f"La cantidad de candidatas mujeres es {cantidad_canditos_f}"
        mensaje_cantidad_candidatos_m = f"La cantidad de candidatos hombres es {cantidad_canditos_m}"
        mensaje_cantidad_candidatos_nb = f"La cantidad de candidatxs NB es {cantidad_canditos_nb}"
        mensaje_nivel_aceptacion = f"El candidato con mayor nivel de aceptacion es {nombre_candidato_mayor_aceptacion} y su genero es {genero_candidato_mayor_aceptacion}"
        mensaje_mujeres_mayores_a_50 = f"La cantidad de mujeres mayores a 50 es {mujeres_mayores_50}"
        mensaje_mujeres_menores_a_50 = f"La cantidad de mujeres menores a 50 es {mujeres_menores_50}"
        mensaje_genero_mayor_candidatos = f"El genero con mas candidatos es {genero_mayor_candidatos}"

        print(mensaje_candidato_mayor_votos)
        print(mensaje_candidato_menor_votos) 
        print(mensaje_promedio_edades)
        print(mensaje_cantidad_votos_total)
        print(mensaje_cantidad_candidatos_f)
        print(mensaje_cantidad_candidatos_m)
        print(mensaje_cantidad_candidatos_nb)
        print(mensaje_nivel_aceptacion)
        print(mensaje_mujeres_mayores_a_50)
        print(mensaje_mujeres_menores_a_50)
        print(mensaje_genero_mayor_candidatos)


        

    



        



        
        
        
        
        
        
        
        #Cuando terminas, preguntas si queres cancelar y cambias el flag









if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
