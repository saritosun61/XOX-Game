from PyQt5.QtWidgets import *
from XOX_arayuz import *
import sys

class XOX(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.t = [self.ui.P_0,self.ui.P_1,self.ui.P_2,self.ui.P_3,
                  self.ui.P_4,self.ui.P_5,self.ui.P_6,self.ui.P_7,self.ui.P_8]
        for i in range(9):
            self.t[i].setText("")
            self.t[i].clicked.connect(self.oyun)
        self.ui.label_O_skor.clear()
        self.ui.label_X_skor.clear()
        self.ui.label_O_oyuncusu.clear()
        self.ui.label_X_oyuncusu.clear()
        self.ui.action_basla.triggered.connect(self.basla)
        self.ui.action_cikis.triggered.connect(self.cikis)
    
    def cikis(self):
        pencere.close()
        uygulama.quit()
        sys.exit()
    def basla(self):
        isim_X = QInputDialog.getText(self,"X Oyuncusu","X oyuncusunun ismini yazınız.")
        self.ui.label_X_oyuncusu.setText(isim_X[0])
        isim_O = QInputDialog.getText(self,"O Oyuncusu","O oyuncusunun ismini yazınız.")
        self.ui.label_O_oyuncusu.setText(isim_O[0])
        self.ui.action_basla.setDisabled(True)
        self.skor_X = 0
        self.skor_O = 0
        self.ui.label_X_skor.setText(str(self.skor_X))
        self.ui.label_O_skor.setText(str(self.skor_O))
        QMessageBox.information(self,"Oyun",f"Oyuna X oyuncusu olarak {isim_X[0]} başlayacak!")
        self.sıra = "X"
        self.k = ["" for _ in range(9)]

        self.ui.label_X_oyuncusu.setStyleSheet("font-weight:bold;")
        self.ui.label_X_oyuncusu.setStyleSheet("color:red;")

    def oyun(self):
        self.c = int(self.sender().objectName()[2])
        if self.k[self.c] == "":
            if self.sıra == "X":
                self.k[self.c] = "X"
                self.t[self.c].setText("X")
                self.kontrol()
            else:
                self.k[self.c] = "O"
                self.t[self.c].setText("O")
                self.kontrol()
        else:
            QMessageBox.information(self,"Oyun","Daha önce orası oynandı, başka yer seçiniz!")
    def kontrol(self):
        if self.k[0]==self.k[1]==self.k[2] and self.k[1] != "":
            self.kazanan()
        elif self.k[3]==self.k[4]==self.k[5] and self.k[4] != "":
            self.kazanan()
        elif self.k[6]==self.k[7]==self.k[8] and self.k[6] != "":
            self.kazanan()
        elif self.k[0]==self.k[3]==self.k[6] and self.k[6] != "":
            self.kazanan()
        elif self.k[1]==self.k[4]==self.k[7] and self.k[1] != "":
            self.kazanan()
        elif self.k[2]==self.k[5]==self.k[8] and self.k[5] != "":
            self.kazanan()
        elif self.k[0]==self.k[4]==self.k[8] and self.k[4] != "":
            self.kazanan()
        elif self.k[2]==self.k[4]==self.k[6] and self.k[6] != "":
            self.kazanan()
        elif not "" in self.k:
            self.berabere()
        else:
            if self.sıra == "X":
                self.sıra = "O"
                self.ui.label_X_oyuncusu.setStyleSheet("font-weight:normal;")
                self.ui.label_X_oyuncusu.setStyleSheet("color:black;")
                self.ui.label_O_oyuncusu.setStyleSheet("font-weight:bold;")
                self.ui.label_O_oyuncusu.setStyleSheet("color:red;")
            else:
                self.sıra = "X"
                self.ui.label_O_oyuncusu.setStyleSheet("font-weight:normal;")
                self.ui.label_O_oyuncusu.setStyleSheet("color:black;")
                self.ui.label_X_oyuncusu.setStyleSheet("font-weight:bold;")
                self.ui.label_X_oyuncusu.setStyleSheet("color:red;")
    def kazanan(self):
        QMessageBox.information(self,"Kazanan",f"Kazanan {self.sıra} oyuncusu",QMessageBox.Ok)
        if self.sıra == "X":
            self.skor_X += 1
            self.ui.label_X_skor.setText(str(self.skor_X))
        else:
            self.skor_O += 1
            self.ui.label_O_skor.setText(str(self.skor_O))
        self.devam()
    def berabere(self):
        QMessageBox.information(self,"Berabere",f"Oyun berabere bitti!",QMessageBox.Ok)
        self.devam()
    def devam(self):
        yanıt = QMessageBox.question(self,"Oyun","Devam etmek ister misiniz?",QMessageBox.Yes|QMessageBox.No)
        if yanıt == QMessageBox.Yes:
            self.yeniden()
        else:
            self.cikis()
    def yeniden(self):
        self.k = ["" for _ in range(9)]
        for i in range(9):
            self.t[i].setText("")
        if self.sıra == "X":
            self.sıra = "O"
        else:
            self.sıra = "X"

if __name__ == "__main__":
    uygulama = QApplication(sys.argv)
    pencere = XOX()
    pencere.show()
    sys.exit(uygulama.exec_())