  
class Lista:

    # Usamos un def para poder crear un objeto
    def __init__(self,id,contenido,o_ordenar,o_buscar,numeros_busqueda):

        self.id = id
        self.contenido = contenido
        self.o_ordenar = o_ordenar
        self.o_buscar = o_buscar
        self.numeros_busqueda = numeros_busqueda

    # Método Get de toda la vida, para poder acceder a la info
    # No vamos a emplear set porque no vamos a guardar info una vez creado el objeto

    def getId(self):
        return self.id

    def getContenido_lista(self):
        return self.contenido

    def getContenido(self):
        Listita = self.contenido
        Cadena_enviar=" ".join(Listita)
        return Cadena_enviar
    
    def getO_ordenar(self):
        return self.o_ordenar
    
    def getO_buscar(self):
        return self.o_buscar

    def getNumeros_busqueda(self):
        return str(self.numeros_busqueda)
    
    def getContenido_ordenado(self):
        Listita = self.contenido
        Listita.sort()
        Cadena_enviar=" ".join(Listita)
        return Cadena_enviar

    def getPosiciones(self):
        a=self.contenido
        s=self.numeros_busqueda
        m="No encontrado"
        elegidos=[]
        for i in range(len(a)):
            if int(a[i]) == int(s):
                elegidos.append(str(i+1))
        if len(elegidos)>0:
            m= " ".join(elegidos)
        return m






