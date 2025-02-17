class Empleado:
    def __init__(self):
        self.nombre = self.__class__.__name__
    
    def comenzar_jornada(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases")
    
    def terminar_jornada(self):
        print(f"{self.nombre} ha terminado su jornada laboral.")
    
    def marcar_jornada(self, accion):
        if accion == "comenzar":
            self.comenzar_jornada()
        elif accion == "terminar":
            self.terminar_jornada()
        else:
            print("Acción no válida.")

class Profesor(Empleado):
    def comenzar_jornada(self):
        print(f"El {self.nombre} comienza a preparar las lecciones y atender a los estudiantes.")

class Administrativo(Empleado):
    def comenzar_jornada(self):
        print(f"El {self.nombre} comienza a revisar los documentos y gestionar las tareas administrativas.")

class Mantenimiento(Empleado):
    def comenzar_jornada(self):
        print(f"El {self.nombre} comienza a inspeccionar y reparar las instalaciones.")

empleados = [Profesor(), Administrativo(), Mantenimiento()]
for empleado in empleados:
    empleado.marcar_jornada("comenzar")
for empleado in empleados:
    empleado.marcar_jornada("terminar")
