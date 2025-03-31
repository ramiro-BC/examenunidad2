from PyQt6.QtWidgets import QApplication, QMainWindow,QLabel,QWidget, \
QGridLayout,QHBoxLayout,QVBoxLayout,QPushButton
import sys
from PyQt6.QtCore import QRunnable, QThreadPool, pyqtSignal as Signal, \
QObject, Qt

class Caja(QLabel):#heredamos qlabel
    def __init__ (self, color):
        super().__init__()
        self.setStyleSheet(f"background-color:{color}")

class worker_signal(QObject): #entrega recados de lo que se debe modificar
    luz_roja=Signal(bool)
    luz_amarilla=Signal(bool)
    luz_verde=Signal(bool)
    luz_azul=Signal(bool)
    def __init__(self):
        super().__init__()

class Worker(QRunnable): #clase que modifica interfaz
    def __init__(self):
        super().__init__()
        self.signals=worker_signal()
    def prender_luz_roja(self,estado:bool=False):
        try:
            self.signals.luz_roja.emit(estado)
        except Exception as e:
            print("se obtuvo un error al emitir la señal")

    def prender_luz_amarilla(self,estado:bool=False):
        try:
            self.signals.luz_amarilla.emit(estado)
        except Exception as e:
            print("se obtuvo un error al emitir la señal")

    def prender_luz_verde(self,estado:bool=False):
        try:
            self.signals.luz_verde.emit(estado)
        except Exception as e:
            print("se obtuvo un error al emitir la señal")

    def prender_luz_azul(self,estado:bool=False):
        try:
            self.signals.luz_azul.emit(estado)
        except Exception as e:
            print("se obtuvo un error al emitir la señal")


class Ventana(QMainWindow):#heredamos ventana
    def __init__ (self):
        super().__init__()
       
        contenedor0=QGridLayout()
        widget=QWidget()

        self.resize(350,250)
        self.setWindowTitle("SEMAFORO")
        widget.setLayout(contenedor0)
        self.setCentralWidget(widget)

        self.caja=Caja("gray")
        self.caja1=Caja("black")
        caja2=Caja("green")

        layautV1=QVBoxLayout()
        layoutV2=QVBoxLayout()
      
        self.indivcvadored=self.crear_indicador("red")
        self.indivcvadoamarilo=self.crear_indicador("yellow")
        self.indivcvadorverde=self.crear_indicador("green")
        self.indivcvadorazul=self.crear_indicador("blue")
        self.boton1=self.crear_indicador("red")
        self.boton2=self.crear_indicador("yellow")
        
        

        layautV1.addWidget(self.indivcvadored)
        layautV1.addWidget(self.indivcvadoamarilo)
        layautV1.addWidget(self.indivcvadorverde)
        layautV1.addWidget(self.indivcvadorazul)

        layoutV2.addWidget(self.boton1)
        layoutV2.addWidget(self.boton2)

        contenedor0.addWidget(self.caja1,0,2,4,1)
        contenedor0.addWidget(self.caja,0,0,4,1)
        contenedor0.addLayout(layoutV2,0,0)
        contenedor0.addLayout(layautV1,0,2)
        

        ##contenedor0.addWidget(caja1,0,1)
        ##contenedor0.addWidget(caja2,1,0,1,2)
        #enlazamos con el worker
        self.threadPool=QThreadPool()
        self.worker=Worker()
        self.worker.signals.luz_roja.connect(self.cambiar_inidicador_rojo)
        self.worker.signals.luz_amarilla.connect(self.cambiar_inidicador_amarillo)
        self.worker.signals.luz_verde.connect(self.cambiar_inidicador_verde)
        self.worker.signals.luz_azul.connect(self.cambiar_inidicador_azul)

    def cambiar_inidicador_rojo(self,estado:bool):
        if estado:
            self.modificar_indicador(self.indivcvadored,"red")
        else:
            self.modificar_indicador(self.indivcvadored,"white")
    
    def cambiar_inidicador_amarillo(self,estado:bool):
        if estado:
            self.modificar_indicador(self.indivcvadoamarilo,"yellow")
        else:
            self.modificar_indicador(self.indivcvadoamarilo,"white")

    def cambiar_inidicador_verde(self,estado:bool):
        if estado:
            self.modificar_indicador(self.indivcvadorverde,"green")
        else:
            self.modificar_indicador(self.indivcvadorverde,"white")

    def cambiar_inidicador_azul(self,estado:bool):
        if estado:
            self.modificar_indicador(self.indivcvadorazul,"blue")
        else:
            self.modificar_indicador(self.indivcvadorazul,"white")

    def modificar_indicador (self,indicador,color):
        indicador.setStyleSheet(f"""
                    background-color: {color}; border-radius: 50""")
        
    def crear_indicador(self, color:str="gray"):
         micajasera= QLabel()
         micajasera.setStyleSheet(f"""
                    background-color: {color}; border-radius: 50""")
         micajasera.setFixedSize(100,100)
         return micajasera
    
    def obtener_worker(self):
        return self.worker

def main ():
    print("dentro de main")
    app = QApplication(sys.argv)
    ventana =Ventana()
    ventana.show()
    sys.exit(app.exec())
if __name__== "__main__":
    main()