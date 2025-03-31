
from PyQt6.QtWidgets import QApplication 
from PyQt6.QtGui import QKeyEvent
from PyQt6.QtCore import Qt
import sys
from interfaz import Ventana #importamosinterfaz
from controlsem import Semaforo #importamos control
class Inicio (Ventana): #escribimos todo el codigo que queremos que se inicie
    def __init__(self):
        super().__init__()
        semaforo = Semaforo() 
        semaforo.inuiciar()
        ##semaforo.establecer_worker()
        semaforo.establecer_worker(self.obtener_worker())

    
def main ():
    print("dentro de main")
    app = QApplication(sys.argv)
    ventana =Inicio()
    ventana.show()
    sys.exit(app.exec())

if __name__== "__main__":
    main()
    