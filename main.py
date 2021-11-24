import pickle
from tkinter import *
from tkinter import messagebox

from ClaseVehiculos import ClaseVehiculos

vehiculo=[]
#Comprobamos si el fichero existe, tiene que leerlo antes para que cargue lo que habia en el array y no te lo borre
try:
    with open("ficheroV", "rb") as fV:
        #Para que lo meta en el array con la variable
        vehiculo = pickle.load(fV)
except:
    None
#FUNCIONES
def insertar():
    if (len(entradaMarca.get().strip()) !=0 and len(entradaModelo.get().strip())!=0):##strip comprueba los espacios
        objetoVehiculo=ClaseVehiculos(entradaModelo.get(), entradaMarca.get()) #Creamos el objeto
        vehiculo.append(objetoVehiculo) ##metemos el objeto en el array
        fichero = open("ficheroV", "wb") #wb=Escritura en binario
        pickle.dump(vehiculo, fichero) #Escribe en el fichero el array, en mi objeto de fichero
        fichero.close()
        del (fichero) #lo elimina de memoria
        messagebox.showinfo("Insertado","Insertado correctamente")
    else:
        messagebox.showerror("Error","Faltan campos por rellenar")

def mostrar():
    try:
        with open("ficheroV", "rb") as fV:
            #Para que lo meta en el array con la variable
            vehiculo=pickle.load(fV)
            ventana2=Toplevel() ##Para que salte la nueva ventana encima
            ventana2.title("Fichero Vechiculos")
            ficheroTexto = Text(ventana2, width=40, height=20) ##Creamos la variable del fichero, donde se va a usar y tamaño
            for i in range(len(vehiculo)):
                ficheroTexto.insert(INSERT, "Marca: "+ vehiculo[i].marca + "        Modelo: " + vehiculo[i].modelo + "\n") ##para insertar en el fichero lo que hay dentro del array
            ficheroTexto.grid(row=1, column=1)
    except:
        messagebox.showerror("Error", "Error al leer el fichero")

def eliminar():
    if(len(entradaMarca.get().strip()) != 0 and len(entradaModelo.get().strip()) != 0):
        vehiculo.remove(ClaseVehiculos(marca=entradaMarca.get(), modelo=entradaModelo.get()))
        fichero = open("ficheroV", "wb")  # wb=Escritura en binario
        pickle.dump(vehiculo, fichero)  # Escribe en el fichero el array, en mi objeto de fichero
        fichero.close()
        del (fichero)  # lo elimina de memoria
        messagebox.showinfo("Insertado", "Insertado correctamente")
    else:
        messagebox.showerror("Error", "Faltan campos por rellenar")









#INTERFAZ
#abrir la ventana
ventana = Tk()
ventana.title("Vehiculos")
#CREAMOS LAS VARIABLES PARA ALMACENAR DATOS
marca= StringVar()
modelo=StringVar()


#INTRODDUCIR DATOS
etiquetaMarca = Label(ventana, text="Marca: ", font=18)
entradaMarca = Entry(ventana, textvariable=marca, font=18)
etiquetaMarca.grid(row=1, column=1)
entradaMarca.grid(row=1, column=2)


etiquetaModelo = Label(ventana, text="Modelo: ", font=18)
entradaModelo= Entry(ventana, textvariable=modelo, font=18)
etiquetaModelo.grid(row=2, column=1)
entradaModelo.grid(row=2, column=2)

#BOTONES
botonInsertar = Button(ventana, text="Insertar", command=insertar, width=20, bg="Black", fg="White")
botonInsertar.grid(row=3, column=2)

botonMostrar = Button(ventana, text="Mostrar", command=mostrar, width=20, bg="Black", fg="White")
botonMostrar.grid(row=4, column=2)

botonEliminar = Button(ventana, text="Eliminar", command=eliminar, width=20, bg="Black", fg="White")
botonEliminar.grid(row=5, column=2)


#ABRIR VENTANA
ventana.mainloop()
