# Sistema Experto para Diagnóstico de Problemas en Computadoras
# Autor: Asistente IA
# Descripción: Sistema básico que diagnostica problemas comunes en computadoras

class SistemaExpertoComputadoras:
    def __init__(self):
        self.sintomas = {}
        self.diagnostico = ""
        self.confianza = 0
        
    def inicializar_base_conocimiento(self):
        """Define las reglas del sistema experto"""
        self.reglas = [
            {
                'condiciones': ['no_enciende', 'luces_apagadas'],
                'diagnostico': 'Problema de alimentación eléctrica',
                'solucion': 'Verificar cable de corriente y fuente de poder',
                'confianza': 90
            },
            {
                'condiciones': ['enciende', 'no_imagen', 'ventiladores_funcionan'],
                'diagnostico': 'Problema con la tarjeta gráfica o monitor',
                'solucion': 'Revisar conexiones del monitor y tarjeta de video',
                'confianza': 85
            },
            {
                'condiciones': ['enciende', 'pitidos_continuos'],
                'diagnostico': 'Error en memoria RAM',
                'solucion': 'Revisar y recolocar módulos de memoria',
                'confianza': 88
            },
            {
                'condiciones': ['muy_lento', 'mucho_ruido_ventilador'],
                'diagnostico': 'Sobrecalentamiento del procesador',
                'solucion': 'Limpiar ventiladores y aplicar pasta térmica',
                'confianza': 75
            },
            {
                'condiciones': ['pantalla_azul', 'reinicios_aleatorios'],
                'diagnostico': 'Problema de software o drivers',
                'solucion': 'Actualizar drivers y escanear en modo seguro',
                'confianza': 70
            },
            {
                'condiciones': ['no_internet', 'otros_dispositivos_funcionan'],
                'diagnostico': 'Problema de configuración de red',
                'solucion': 'Reiniciar adaptador de red y verificar configuración',
                'confianza': 80
            }
        ]
    
    def hacer_preguntas(self):
        """Recopila información del usuario"""
        print("=== SISTEMA EXPERTO - DIAGNÓSTICO DE COMPUTADORAS ===")
        print("Responda con 'si' o 'no' a las siguientes preguntas:\n")
        
        preguntas = {
            'no_enciende': '¿La computadora no enciende para nada?',
            'luces_apagadas': '¿No se ven luces encendidas en la computadora?',
            'enciende': '¿La computadora enciende pero tiene problemas?',
            'no_imagen': '¿No aparece imagen en el monitor?',
            'ventiladores_funcionan': '¿Escucha que los ventiladores funcionan?',
            'pitidos_continuos': '¿Escucha pitidos continuos al encender?',
            'muy_lento': '¿La computadora funciona muy lenta?',
            'mucho_ruido_ventilador': '¿Los ventiladores hacen mucho ruido?',
            'pantalla_azul': '¿Aparece pantalla azul de error?',
            'reinicios_aleatorios': '¿Se reinicia sola la computadora?',
            'no_internet': '¿No tiene conexión a internet?',
            'otros_dispositivos_funcionan': '¿Otros dispositivos sí tienen internet?'
        }
        
        for clave, pregunta in preguntas.items():
            while True:
                respuesta = input(f"{pregunta} ").lower().strip()
                if respuesta in ['si', 'sí', 's', 'yes', 'y']:
                    self.sintomas[clave] = True
                    break
                elif respuesta in ['no', 'n']:
                    self.sintomas[clave] = False
                    break
                else:
                    print("Por favor responda 'si' o 'no'")
    
    def evaluar_reglas(self):
        """Evalúa las reglas contra los síntomas recopilados"""
        mejor_diagnostico = None
        mejor_confianza = 0
        
        for regla in self.reglas:
            coincidencias = 0
            total_condiciones = len(regla['condiciones'])
            
            # Verificar cuántas condiciones se cumplen
            for condicion in regla['condiciones']:
                if self.sintomas.get(condicion, False):
                    coincidencias += 1
            
            # Calcular porcentaje de coincidencia
            porcentaje_coincidencia = (coincidencias / total_condiciones) * 100
            
            # Si todas las condiciones se cumplen, es un diagnóstico válido
            if coincidencias == total_condiciones:
                confianza_ajustada = regla['confianza']
                if confianza_ajustada > mejor_confianza:
                    mejor_confianza = confianza_ajustada
                    mejor_diagnostico = regla
        
        return mejor_diagnostico, mejor_confianza
    
    def mostrar_diagnostico(self, diagnostico, confianza):
        """Muestra el resultado del diagnóstico"""
        print("\n" + "="*50)
        print("RESULTADO DEL DIAGNÓSTICO")
        print("="*50)
        
        if diagnostico:
            print(f"Diagnóstico: {diagnostico['diagnostico']}")
            print(f"Confianza: {confianza}%")
            print(f"Solución recomendada: {diagnostico['solucion']}")
            
            if confianza >= 80:
                print("🟢 Diagnóstico con alta confianza")
            elif confianza >= 60:
                print("🟡 Diagnóstico con confianza media")
            else:
                print("🔴 Diagnóstico con baja confianza")
        else:
            print("❌ No se pudo determinar el problema con los síntomas proporcionados.")
            print("Recomendación: Consulte con un técnico especializado.")
    
    def ejecutar(self):
        """Método principal que ejecuta el sistema experto"""
        self.inicializar_base_conocimiento()
        self.hacer_preguntas()
        diagnostico, confianza = self.evaluar_reglas()
        self.mostrar_diagnostico(diagnostico, confianza)
        
        print("\n¿Desea realizar otro diagnóstico? (si/no)")
        if input().lower() in ['si', 'sí', 's', 'yes', 'y']:
            self.sintomas = {}  # Limpiar síntomas
            self.ejecutar()

# Función principal
def main():
    print("Iniciando Sistema Experto...")
    sistema = SistemaExpertoComputadoras()
    sistema.ejecutar()
    print("\n¡Gracias por usar el Sistema Experto!")

# Ejecutar el programa
if __name__ == "__main__":
    main()