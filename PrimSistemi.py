import sys 
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtGui,uic
class PrimSistemi(QtGui.QMainWindow):
    def __init__(self):
        super(PrimSistemi,self).__init__()
        uic.loadUi('PrimSistemiQt.ui',self)
        self.connect(self.hesaplaButon, SIGNAL("pressed()"),self.ciroHesapla)
        self.show()

    
        
        
    def ciroHesapla(self):
        gelir=self.gelirText.text()
        gider=self.giderText.text()
        ciro=int(gelir)-int(gider)
        prim=int(ciro)/100
        mudur=int(prim)*0.25
        muduryar=int(prim)*0.15
        kasiyer=int(prim)*0.10
        satisDanismani=int(prim)*0.17
        satisDanismani_2=int(prim)*0.17
        satisDanismani_3=int(prim)*0.16
        self.mdrLabel.setText(str(mudur))
        self.mdyLabel.setText(str(muduryar))
        self.ksyrLabel.setText(str(kasiyer))
        self.sdLabel.setText(str(satisDanismani))
        self.sdLabel_2.setText(str(satisDanismani_2))
        self.sdLabel_3.setText(str(satisDanismani_3))
        self.ciroLabel.setText(str(ciro))
        

        
    def build(self):
        self.statusBar()

uyg=QApplication([])
pencere=PrimSistemi()
pencere.resize(450,600)
pencere.move(500,100)
pencere.show()
uyg.exec_
