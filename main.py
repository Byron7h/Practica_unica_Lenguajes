if __name__ == '__main__':

    # el filedialos de tkinter nos permite abrir un selector de archivos
    # devuelve la dirección del archivo seleccionado 
    from tkinter import filedialog
    from Listas import Lista 
    listas_registradas=[]

#-------------------------------Leer Archivo y guardar info en objeto -----------------------
    def Leer_archivo(eje):       
        #Primero abrimos el archivo y le decimos para que lo abrimos    
        archivo = open(eje)

        for linea in archivo.readlines():  
            # Splita(=) para poder separar el nombre 
            # En cadena vamos dejando el resto en forma de cadena
            cadena = str(linea).split("=")
            nombre =cadena[0]
            cadena= str(cadena[1])
            

            #Encontramos la posición anterior al ORDENAR o BUSCAR Para poder dividir la
            #cadena en este punto, de acá sacamos el cotenido y las operaciones
            pos=-1
            for caracter in cadena:
                if caracter =="O" or caracter == "B":
                    break
                else:
                    pos=pos+1
            contenido = str(cadena[:pos])
            operaciones = cadena[pos:]


            #Modificamos el contenido de tal forma que nos queden solo los datos separados por coma           
            lista_contenido= []
            for x in range(0,len(contenido)):
                if contenido[x] !=" ":
                    lista_contenido.append(contenido[x])
            #Convertimos la lista sin espacios en una cadena para hacerle un split por comas
            contenido="".join(lista_contenido)
            lista_contenido= contenido.split(",")


            #Analizamos las operaciones que nos da el archivo
            buscar="BUSCAR" in operaciones
            ordenar="ORDENAR" in operaciones
            lista_operaciones =[]
            for x in range(0,len(operaciones)):
                if operaciones[x] !=" ":
                    lista_operaciones.append(operaciones[x])
            #Convertimos la lista sin espacios en una cadena para hacerle un split por comas
            #si fuera necesario
            operaciones="".join(lista_operaciones)
              

            #Encontramos el dato a encontrar si se reunen las condiciones
            numero=""
            if buscar and ordenar:
                lista_operaciones= operaciones.split(",")
                if "BUSCAR" in lista_operaciones[0]:
                    numero = str(lista_operaciones[0]).lstrip("BUSCAR" )
                else:
                    numero = str(lista_operaciones[1]).lstrip("BUSCAR" )
               
            elif buscar:
                numero = operaciones.lstrip("BUSCAR" )

            listas_registradas.append(Lista(nombre,lista_contenido, ordenar ,buscar, numero))
        archivo.close()



    def ordenamientoPorSeleccion(unaLista):
        # En el len es descendente, desde len -1 (porque se toma en cuenta el 0)
        # hasta el -1 es para que tome en cuenta el 01 
        for llenarRanura in range(len(unaLista)-1,0,-1):
            posicionDelMayor=0
            for ubicacion in range(1,llenarRanura+1):
                if unaLista[ubicacion]>unaLista[posicionDelMayor]:
                    posicionDelMayor = ubicacion

            temp = unaLista[llenarRanura]
            unaLista[llenarRanura] = unaLista[posicionDelMayor]
            unaLista[posicionDelMayor] = temp
        return(unaLista)
        
#-------------------------------Leer Archivo y guardar info en objeto -----------------------
    def Listas_ordenadas():

        global listas_registradas
        print("")
        print(" :::::::::::::::::  LISTAS ORDENADAS  :::::::::::::::::: ")
        print("")
        for i in range(len(listas_registradas)):
            if listas_registradas[i].getO_ordenar():
                lista_desordenada= listas_registradas[i].getContenido_lista()
                lista_desordenada = ordenamientoPorSeleccion(lista_desordenada) 
                lista_ordenada=" ".join(lista_desordenada)
                print("Lista: ", listas_registradas[i].getId())
                print("Contenido Ordenado :",lista_ordenada)
                print("")

    def Listas_busqueda():

        global listas_registradas
        print("")
        print(" ::::::::::::::::: LISTAS CON BUSQUEDA ::::::::::::::::: ")
        print("")

        for m in range(len(listas_registradas)):
            if listas_registradas[m].getO_buscar():

                print("Lista: ", listas_registradas[m].getId())
                print("Contenido:",listas_registradas[m].getContenido())
                print("Dato a buscar:",listas_registradas[m].getNumeros_busqueda(),"Se encuentra en las posiciones ", listas_registradas[m].getPosiciones() )
                print("")

    def Listas_todas():

        global listas_registradas
        print("")
        print(" :::::::::::::::::: TODAS LAS LISTAS ::::::::::::::::::: ")
        print("")
        for n in range(len(listas_registradas)):
            print("Lista: ", listas_registradas[n].getId())
            print("Contenido:",listas_registradas[n].getContenido())

            if listas_registradas[n].getO_buscar():
                print("Dato a buscar:",listas_registradas[n].getNumeros_busqueda(),"Se encuentra en las posiciones ", listas_registradas[n].getPosiciones() )

            if listas_registradas[n].getO_ordenar():
                lista_desordenada= listas_registradas[n].getContenido_lista()
                lista_desordenada = ordenamientoPorSeleccion(lista_desordenada) 
                lista_ordenada=" ".join(lista_desordenada)
                print("Contenido Ordenado :",lista_ordenada)
        
            print("")


    def Documento():
        f = open('doc.html','w')

        mensaje = """
        <link href="estilo.css" rel="stylesheet">
        <h1>Listas Registradas</h1>
        <p>Se presentan a continuación las listas registradas y su contenido, además de las operaciones que se les realizó dependiendo de los parámetros dados para cada una de ellas, siendo estas el ordenamiento ascendente del contenido y/o búsqueda que algún elemento en este, devolviendo las posiciones en las que este se encuentre, en caso de no estar presente devolverá “No encontrado”.
        </p>
        """
        f.write(mensaje)


        for n in range(len(listas_registradas)):

            f.write("""<h3>""")
            f.write(str(listas_registradas[n].getId()))
            f.write("""</h3>\n""")

            f.write("""<div class="cols-3">\n""")
            f.write("""  <div class="cols-span-3">\n""")
            f.write("""    <div class="box">""")
            f.write("Contenido:")
            f.write(str(listas_registradas[n].getContenido()))
            f.write("""</div>\n""")
            f.write("""  </div>\n""")
            f.write("""</div>\n""")

            if listas_registradas[n].getO_buscar():
    
                f.write("""<div class="cols-4">\n""")
                f.write("""  <div class="cols-span-1">\n""")
                f.write("""    <div class="box">""")
                f.write("Buscamos:")
                f.write(str(listas_registradas[n].getNumeros_busqueda()))
                f.write("""</div>\n""")
                f.write("""  </div>\n""")
                f.write("""  <div class="cols-span-3">\n""")
                f.write("""   <div class="box">Posiciones donde se encontró: """)
                f.write(str(listas_registradas[n].getPosiciones()))
                f.write("""</div>""")                                  
                f.write("""  </div>\n""")
                f.write("""</div>\n""")


            if listas_registradas[n].getO_ordenar():
                lista_desordenada = listas_registradas[n].getContenido_lista()
                lista_desordenada = ordenamientoPorSeleccion(lista_desordenada) 
                lista_ordenada=" ".join(lista_desordenada)

                f.write("""<div class="cols-3">\n""")
                f.write("""  <div class="cols-span-3">\n""")
                f.write("""    <div class="box">Contenido Ordenado:""")
                f.write(str(lista_ordenada))
                f.write("""</div>\n""")
                f.write("""  </div>\n""")
                f.write("""</div>\n""")
        f.close()


    def Menu_principal():
        print("")
        print(" :::::: Ingrese el número de la opción a ejecutar ::::::")
        print("1. Cargar archivo de entrada")
        print("2. Desplegar listas ordenadas")
        print("3. Desplegar búsquedas")
        print("4. Desplegar todas")
        print("5. Desplegar todas a archivo")
        print("6. Salir")
        print("")
        a = int(input())
        if a==1:
            #acá va un try except
            nombre_archivo =  filedialog.askopenfilename(title = "Select file")
            Leer_archivo(nombre_archivo)
            Menu_principal()
        elif a==2:
            Listas_ordenadas()
            Menu_principal()
        elif a==3:
            Listas_busqueda()
            Menu_principal()
        elif a==4:
            Listas_todas()
            Menu_principal()
        elif a==5:
            Documento()
            Menu_principal()
        else:
            print("Gracias por usar el programa")


    Menu_principal()
