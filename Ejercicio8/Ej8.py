# Un alumno desea saber cuál será su calificación final en la materia de Algoritmos. Dicha calificación se compone de los siguientes porcentajes:
# •	55% del promedio de sus tres calificaciones parciales.
# •	30% de la calificación del examen final.
# •	15% de la calificación de un trabajo final.
#  

#Método para calcular la nota final de un alumno
def calcularNotaFinal():
    
    examen1=float(input("Dime la calificacion del primer examen parcial -->"))
    examen2=float(input("Dime la calificacion del segundo examen parcial-->"))
    examen3=float(input("Dime la calificacion del tercer examen parcial-->"))
    
    examenFinal=float(input("Dime la calificacion del examen final -->"))
    
    trabajoFinal=float(input("Dime la calificacion del trabajo final -->"))
    
    promedioParciales = (examen1 + examen2 + examen3)/3
    
    calificacionFinal = (promedioParciales*0.55) + (examenFinal * 0.3) + (trabajoFinal * 0.15)
    
    print("La calificación final es ", calificacionFinal)
    
    
#Método main para sus respectivos métodos
if __name__ == "__main__":
    calcularNotaFinal()