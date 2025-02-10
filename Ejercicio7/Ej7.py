# Hacer un programa que muestre un cronometro y un temporizador, indicando las horas, minutos y segundos.
# Incluir botón que reinicia el cronómetro, restableciendo las horas, minutos y segundos a cero.
# Botón temporizador que inicia desde un tiempo específico (5 minutos) y cuenta hacia atrás.


#Importamos tktinter para trabajar con la interfaz gráfica
import tkinter as tk

#Función para formatear el tiempo
def formateoTiempo(segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos = segundos % 60
    return f"{horas:02}:{minutos:02}:{segundos:02}"

#Creamos la clase Aplicacion donde se desarrollara el cronómetro
class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Cronómetro y Temporizador")  #Titulo 

        #Cronómetro
        self.cronometroRunning = False  #Estado del cronómetro 
        self.cronometroTime = 0  #Tiempo del cronómetro

        #Temporizador
        self.temporizadorRunning = False  #Estado del temporizador 
        self.temporizadorTime = 5 * 60  #Tiempo del temporizador en segundos

        #Etiquetas del tiempo del cronómetro y temporizador
        self.cronometroLabel = tk.Label(root, text="00:00:00", font=("Times New Roman", 25))
        self.cronometroLabel.pack(pady=10)

        self.temporizadorLabel = tk.Label(root, text="00:05:00", font=("Times New Roman", 25))
        self.temporizadorLabel.pack(pady=10)

        #Botones para controlar el cronómetro
        self.btnCronoIniciar = tk.Button(root, text="Iniciar Cronómetro", command=self.iniciarCronometro,bg="blue", fg="white")
        self.btnCronoIniciar.pack(pady=5)

        self.btnCronoPausar = tk.Button(root, text="Pausar Cronómetro", command=self.pausarCronometro,bg="blue", fg="white")
        self.btnCronoPausar.pack(pady=5)

        self.btnCronoReset = tk.Button(root, text="Reiniciar Cronómetro", command=self.reiniciarCronometro,bg="blue", fg="white")
        self.btnCronoReset.pack(pady=5)

        #Botones para controlar el temporizador
        self.btnTempIniciar = tk.Button(root, text="Iniciar Temporizador", command=self.iniciarTemporizador,bg="green", fg="white")
        self.btnTempIniciar.pack(pady=5)

        self.btnTempPausar = tk.Button(root, text="Pausar Temporizador", command=self.pausarTemporizador,bg="green", fg="white")
        self.btnTempPausar.pack(pady=5)

        self.btnTempReset = tk.Button(root, text="Reiniciar Temporizador", command=self.reiniciarTemporizador,bg="green", fg="white")
        self.btnTempReset.pack(pady=5)

    #Método para actualizar el cronómetro cada segundo
    def actualizarCronometro(self):
        if self.cronometroRunning:
            self.cronometroTime += 1  #Aumenta el tiempo del cronómetro
            self.cronometroLabel.config(text=formateoTiempo(self.cronometroTime))
            self.root.after(1000, self.actualizarCronometro) 

    #Método para iniciar el cronómetro
    def iniciarCronometro(self):
        if not self.cronometroRunning:
            self.cronometroRunning = True
            self.actualizarCronometro()  #Actualiza el cronómetro

    #Método para pausar el cronómetro
    def pausarCronometro(self):
        self.cronometroRunning = False

    #Método para reiniciar el cronómetro
    def reiniciarCronometro(self):
        self.cronometroRunning = False
        self.cronometroTime = 0
        self.cronometroLabel.config(text="00:00:00")  #Reinicia el cronómetro a cero

    #Método para actualizar el temporizador cada segundo
    def actualizarTemporizador(self):
        if self.temporizadorRunning and self.temporizadorTime > 0:
            self.temporizadorTime -= 1  #Resta el tiempo del temporizador
            self.temporizadorLabel.config(text=formateoTiempo(self.temporizadorTime))
            self.root.after(1000, self.actualizarTemporizador)  

    #Método para iniciar el temporizador
    def iniciarTemporizador(self):
        if not self.temporizadorRunning:
            self.temporizadorRunning = True
            self.actualizarTemporizador()  #Actualiza el cronómetro

    #Método para pausar el temporizador
    def pausarTemporizador(self):
        self.temporizadorRunning = False

    #Método para reiniciar el temporizador
    def reiniciarTemporizador(self):
        self.temporizadorRunning = False
        self.temporizadorTime = 5 * 60
        self.temporizadorLabel.config(text="00:05:00")


#Método main para sus respectivos métodos
if __name__ == "__main__":
    root = tk.Tk()  #Crea una la ventana de Tkinter
    app = Aplicacion(root)  #Crea la aplicación
    root.mainloop()  
