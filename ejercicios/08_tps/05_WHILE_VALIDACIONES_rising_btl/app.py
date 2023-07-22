import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Rising BTL. Empresa dedicada a la toma de datos para realizar estadísticas y censos nos pide realizar una carga de datos validada e ingresada 
por ventanas emergentes solamente (para evitar hacking y cargas maliciosas) y luego asignarla a cuadros de textos. 

Los datos requeridos son los siguientes:
    Apellido
    Edad, entre 18 y 90 años inclusive.
    Estado civil, ["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"]
    Número de legajo, numérico de 4 cifras, sin ceros a la izquierda.
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.label0 = customtkinter.CTkLabel(master=self, text="Apellido")
        self.label0.grid(row=0, column=0, padx=20, pady=10)
        self.txt_apellido = customtkinter.CTkEntry(master=self)
        self.txt_apellido.grid(row=0, column=1)

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=1, column=0, padx=20, pady=10)
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=1, column=1)

        self.label2 = customtkinter.CTkLabel(master=self, text="Estado")
        self.label2.grid(row=2, column=0, padx=20, pady=10)
        self.combobox_tipo = customtkinter.CTkComboBox(
            master=self, values=["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"])
        self.combobox_tipo.grid(row=2, column=1, padx=20, pady=10)

        self.label3 = customtkinter.CTkLabel(master=self, text="Legajo")
        self.label3.grid(row=3, column=0, padx=20, pady=10)
        self.txt_legajo = customtkinter.CTkEntry(master=self)
        self.txt_legajo.grid(row=3, column=1)

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        #El combobox lo tenes que pedir por prompt tambien porque no le podes pedir informacion a las barritas que te vienen
        
        flag = True
        while flag:
            apellido = None
            edad_txt = None
            estado_civil = None
            numero_legajo_txt = None

            while apellido == None:
                apellido = prompt(title="Apellido", prompt="Ingrese su apellido")
            
            while edad_txt == None or int(edad_txt) < 18 or int(edad_txt) > 90:
                edad_txt = prompt(title="Edad", prompt="Ingrese la edad")

            while not estado_civil or (estado_civil != "Soltero" and estado_civil != "Soltera" and estado_civil != "Casado" and estado_civil != "Casada" and estado_civil != "Viudo" and estado_civil != "Viuda" and estado_civil != "Divorciado" and estado_civil != "Divorciada"):
                estado_civil = prompt(title="Estado civil", prompt="Ingrese su estado civil")
            
            match estado_civil:
                case "Soltera" | "Soltero":
                    estado_civil_combo  ="Soltero/a"
                case "Casada" | "Casado":
                    estado_civil_combo = "Casado/a"
                case "Divorciada" | "Divorciado":
                    estado_civil_combo = "Divorciado/a"
                case _:
                    estado_civil_combo = "Viudo/a"

            
            while not numero_legajo_txt or int(numero_legajo_txt) < 1000 or int(numero_legajo_txt) > 9999 or numero_legajo_txt.startswith("0"):
                numero_legajo_txt = prompt(title="Numero de legajo", prompt="Ingrese numero de legajo")


            self.txt_apellido.delete(0, "end")
            self.txt_apellido.insert(0, apellido)

            self.txt_edad.delete(0, "end")
            self.txt_edad.insert(0, edad_txt)

            self.combobox_tipo.set(estado_civil_combo)

            self.txt_legajo.delete(0, "end")
            self.txt_legajo.insert(0, numero_legajo_txt)
                

            cancelar = question(title="Cancelar", message="Desea cancelar?")
            if cancelar:
                flag = False


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
