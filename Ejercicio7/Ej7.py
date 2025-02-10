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
        self.cronometro_running = False  #Estado del cronómetro 
        self.cronometro_time = 0  #Tiempo del cronómetro

        #Temporizador
        self.temporizador_running = False  #Estado del temporizador 
        self.temporizador_time = 5 * 60  #Tiempo del temporizador en segundos

        #Etiquetas del tiempo del cronómetro y temporizador
        self.cronometro_label = tk.Label(root, text="00:00:00", font=("Times New Roman", 20))
        self.cronometro_label.pack(pady=10)

        self.temporizador_label = tk.Label(root, text="00:05:00", font=("Times New Roman", 20))
        self.temporizador_label.pack(pady=10)

        #Botones para controlar el cronómetro
        self.btn_crono_iniciar = tk.Button(root, text="Iniciar Cronómetro", command=self.iniciar_cronometro)
        self.btn_crono_iniciar.pack(pady=5)

        self.btn_crono_pausar = tk.Button(root, text="Pausar Cronómetro", command=self.pausar_cronometro)
        self.btn_crono_pausar.pack(pady=5)

        self.btn_crono_reset = tk.Button(root, text="Reiniciar Cronómetro", command=self.reiniciar_cronometro)
        self.btn_crono_reset.pack(pady=5)

        #Botones para controlar el temporizador
        self.btn_temp_iniciar = tk.Button(root, text="Iniciar Temporizador", command=self.iniciar_temporizador)
        self.btn_temp_iniciar.pack(pady=5)

        self.btn_temp_pausar = tk.Button(root, text="Pausar Temporizador", command=self.pausar_temporizador)
        self.btn_temp_pausar.pack(pady=5)

        self.btn_temp_reset = tk.Button(root, text="Reiniciar Temporizador", command=self.reiniciar_temporizador)
        self.btn_temp_reset.pack(pady=5)

    #Método para actualizar el cronómetro cada segundo
    def actualizar_cronometro(self):
        if self.cronometro_running:
            self.cronometro_time += 1  #Aumenta el tiempo del cronómetro
            self.cronometro_label.config(text=formateoTiempo(self.cronometro_time))
            self.root.after(1000, self.actualizar_cronometro) 

    #Método para iniciar el cronómetro
    def iniciar_cronometro(self):
        if not self.cronometro_running:
            self.cronometro_running = True
            self.actualizar_cronometro()  #Actualiza el cronómetro

    #Método para pausar el cronómetro
    def pausar_cronometro(self):
        self.cronometro_running = False

    #Método para reiniciar el cronómetro
    def reiniciar_cronometro(self):
        self.cronometro_running = False
        self.cronometro_time = 0
        self.cronometro_label.config(text="00:00:00")  #Reinicia el cronómetro a cero

    #Método para actualizar el temporizador cada segundo
    def actualizar_temporizador(self):
        if self.temporizador_running and self.temporizador_time > 0:
            self.temporizador_time -= 1  #Resta el tiempo del temporizador
            self.temporizador_label.config(text=formateoTiempo(self.temporizador_time))
            self.root.after(1000, self.actualizar_temporizador)  

    #Método para iniciar el temporizador
    def iniciar_temporizador(self):
        if not self.temporizador_running:
            self.temporizador_running = True
            self.actualizar_temporizador()  #Actualiza el cronómetro

    #Método para pausar el temporizador
    def pausar_temporizador(self):
        self.temporizador_running = False

    #Método para reiniciar el temporizador
    def reiniciar_temporizador(self):
        self.temporizador_running = False
        self.temporizador_time = 5 * 60
        self.temporizador_label.config(text="00:05:00")


#Método main para sus respectivos métodos
if __name__ == "__main__":
    root = tk.Tk()  #Crea una la ventana de Tkinter
    app = Aplicacion(root)  #Crea la aplicación
    root.mainloop()  
