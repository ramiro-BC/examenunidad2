import threading
import time
from temporizador import Temporizador
from PyQt6.QtGui import QKeyEvent
from PyQt6.QtCore import Qt


class Semaforo():
    def __init__(self):
        print("dentro de semaforo")

        self.TON_0=Temporizador("TON_00",12)
        self.TON_1=Temporizador("TON_01",3)
        self.TON_1_1=Temporizador("TON_01",0.8)
        self.TON_1_2=Temporizador("TON_01",0.3)
        self.TON_2=Temporizador("TON_02",10)

        self.TON_az1=Temporizador("TON_03",2)
        self.TON_az2=Temporizador("TON_04",1)
        
        self.finish=1
        self.M0=True
        self.M1=True
        self.aux1=False
        self.aux2=False
        self.luzroja=False
        self.luzamarilla=False
        self.luzverde=False
        self.luzazul=False
        ##worker pra enlace
        self.worker=None
        
        self.tarea=threading.Thread(target= self.semaforo_funcionando)

    def inuiciar(self):
        if self.tarea:
            self.tarea.start() 


    def semaforo_funcionando(self):
        while  self.finish==1:
           #ks print("el se mafor esta funcionando")
            self.TON_0.entrada=self.M0 and not self.TON_2.salida
            self.TON_0.actualizar()
            self.TON_1.entrada=self.M0 and self.TON_0.salida
            self.TON_1.actualizar()

            self.TON_1_1.entrada=self.TON_0.salida and not self.TON_1_2.salida and not self.TON_1.salida
            self.TON_1_1.actualizar()

            self.TON_1_2.entrada=self.TON_1_1.salida
            self.TON_1_2.actualizar()

            self.TON_2.entrada=self.M0 and self.TON_1.salida
            self.TON_2.actualizar()
    #azul
            self.TON_az1.entrada=self.M1 and not self.aux2
            self.aux1=self.M1 and not self.aux2 and self.TON_az1.salida 
            self.TON_az1.actualizar()

            self.TON_az2.entrada=self.M1 and self.aux1
            self.aux2=self.M1 and self.aux1 and self.TON_az2.salida 
            self.TON_az2.actualizar()

            self.luzroja=self.M0 and not self.TON_0.salida
            self.luzamarilla=self.M0 and self.TON_0.salida and not self.TON_1_1.salida and not self.TON_1.salida
            self.luzverde=self.M0 and self.TON_1.salida and not self.TON_2.salida
            self.luzazul=self.M1 and not self.aux1

            print(f"R: {self.luzroja} A: {self.luzamarilla} V: {self.luzverde} Azul: {self.luzazul}")
            #mapeando haci la interfaz
            if self.worker:
                self.worker.prender_luz_roja(self.luzroja)
            if self.worker:
                self.worker.prender_luz_amarilla(self.luzamarilla)
            if self.worker:
                self.worker.prender_luz_verde(self.luzverde)
            if self.worker:
                self.worker.prender_luz_azul(self.luzazul)
            
            
            time.sleep(0.01)
    

    def establecer_worker(self, worker):
        self.worker=worker

    
def main():
    print("dentro de Main")
    semaforo=Semaforo()
    semaforo.inuiciar()

if __name__=="__main__":
    main()