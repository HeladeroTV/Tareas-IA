class RedSemantica:
    def __init__(self):
        # Diccionario para almacenar nodos y sus relaciones
        self.nodos = {}
    
    def agregar_nodo(self, nombre):
        """Agrega un nuevo nodo a la red semántica"""
        if nombre not in self.nodos:
            self.nodos[nombre] = {}
    
    def agregar_relacion(self, nodo1, relacion, nodo2):
        """Establece una relación entre dos nodos"""
        # Asegurarse de que ambos nodos existan
        self.agregar_nodo(nodo1)
        self.agregar_nodo(nodo2)
        
        # Agregar la relación
        if relacion not in self.nodos[nodo1]:
            self.nodos[nodo1][relacion] = []
        
        self.nodos[nodo1][relacion].append(nodo2)
    
    def obtener_relaciones(self, nodo):
        """Obtiene todas las relaciones de un nodo específico"""
        if nodo in self.nodos:
            return self.nodos[nodo]
        return {}
    
    def consultar(self, nodo, relacion):
        """Consulta los nodos relacionados con un nodo mediante una relación específica"""
        if nodo in self.nodos and relacion in self.nodos[nodo]:
            return self.nodos[nodo][relacion]
        return []
    
    def mostrar_red(self):
        """Muestra toda la red semántica"""
        for nodo, relaciones in self.nodos.items():
            print(f"Nodo: {nodo}")
            for relacion, destinos in relaciones.items():
                for destino in destinos:
                    print(f"  --{relacion}--> {destino}")


# Ejemplo de uso con conceptos de animales
if __name__ == "__main__":
    # Crear una red semántica
    red = RedSemantica()
    
    # Agregar nodos y relaciones
    red.agregar_relacion("Animal", "es_un", "Ser vivo")
    red.agregar_relacion("Mamífero", "es_un", "Animal")
    red.agregar_relacion("Ave", "es_un", "Animal")
    red.agregar_relacion("Pez", "es_un", "Animal")
    
    red.agregar_relacion("Perro", "es_un", "Mamífero")
    red.agregar_relacion("Gato", "es_un", "Mamífero")
    red.agregar_relacion("Ballena", "es_un", "Mamífero")
    
    red.agregar_relacion("Águila", "es_un", "Ave")
    red.agregar_relacion("Pingüino", "es_un", "Ave")
    
    red.agregar_relacion("Salmón", "es_un", "Pez")
    
    # Agregar características
    red.agregar_relacion("Mamífero", "característica", "da leche")
    red.agregar_relacion("Ave", "característica", "tiene plumas")
    red.agregar_relacion("Pez", "característica", "vive en agua")
    
    red.agregar_relacion("Perro", "puede", "ladrar")
    red.agregar_relacion("Gato", "puede", "maullar")
    red.agregar_relacion("Águila", "puede", "volar")
    red.agregar_relacion("Pingüino", "puede", "nadar")
    red.agregar_relacion("Pingüino", "no puede", "volar")
    
    # Mostrar la red completa
    print("Red semántica completa:")
    red.mostrar_red()
    
    # Realizar algunas consultas
    print("\nConsultas:")
    print(f"¿Qué es un Perro? {red.consultar('Perro', 'es_un')}")
    print(f"¿Qué es un Mamífero? {red.consultar('Mamífero', 'es_un')}")
    print(f"¿Qué características tienen los mamíferos? {red.consultar('Mamífero', 'característica')}")
    print(f"¿Qué puede hacer un Pingüino? {red.consultar('Pingüino', 'puede')}")
    print(f"¿Qué no puede hacer un Pingüino? {red.consultar('Pingüino', 'no puede')}")