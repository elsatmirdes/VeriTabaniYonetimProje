# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1052, 572)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 0, 1021, 561))
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab_3)
        self.tabWidget_2.setGeometry(QtCore.QRect(0, 0, 1021, 491))
        self.tabWidget_2.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget_2.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.label_3 = QtWidgets.QLabel(self.tab_5)
        self.label_3.setGeometry(QtCore.QRect(480, 30, 131, 31))
        self.label_3.setObjectName("label_3")
        self.personelTelefon = QtWidgets.QLineEdit(self.tab_5)
        self.personelTelefon.setGeometry(QtCore.QRect(30, 190, 113, 31))
        self.personelTelefon.setObjectName("personelTelefon")
        self.personelSoyad = QtWidgets.QLineEdit(self.tab_5)
        self.personelSoyad.setGeometry(QtCore.QRect(30, 110, 113, 31))
        self.personelSoyad.setObjectName("personelSoyad")
        self.personelTC = QtWidgets.QLineEdit(self.tab_5)
        self.personelTC.setGeometry(QtCore.QRect(30, 150, 113, 31))
        self.personelTC.setObjectName("personelTC")
        self.personelAd = QtWidgets.QLineEdit(self.tab_5)
        self.personelAd.setGeometry(QtCore.QRect(30, 70, 113, 31))
        self.personelAd.setObjectName("personelAd")
        self.personelTip = QtWidgets.QLineEdit(self.tab_5)
        self.personelTip.setGeometry(QtCore.QRect(30, 270, 113, 31))
        self.personelTip.setObjectName("personelTip")
        self.personelEmail = QtWidgets.QLineEdit(self.tab_5)
        self.personelEmail.setGeometry(QtCore.QRect(30, 230, 113, 31))
        self.personelEmail.setObjectName("personelEmail")
        self.personelMaas = QtWidgets.QLineEdit(self.tab_5)
        self.personelMaas.setGeometry(QtCore.QRect(30, 310, 113, 31))
        self.personelMaas.setMaxLength(6)
        self.personelMaas.setObjectName("personelMaas")
        self.personelEkle = QtWidgets.QPushButton(self.tab_5)
        self.personelEkle.setGeometry(QtCore.QRect(30, 360, 111, 41))
        self.personelEkle.setObjectName("personelEkle")
        self.label_11 = QtWidgets.QLabel(self.tab_5)
        self.label_11.setGeometry(QtCore.QRect(30, 30, 121, 31))
        self.label_11.setObjectName("label_11")
        self.label_17 = QtWidgets.QLabel(self.tab_5)
        self.label_17.setGeometry(QtCore.QRect(240, 30, 131, 31))
        self.label_17.setObjectName("label_17")
        self.personelSor = QtWidgets.QLineEdit(self.tab_5)
        self.personelSor.setGeometry(QtCore.QRect(240, 70, 113, 31))
        self.personelSor.setObjectName("personelSor")
        self.personelBilAd = QtWidgets.QLabel(self.tab_5)
        self.personelBilAd.setGeometry(QtCore.QRect(240, 160, 141, 21))
        self.personelBilAd.setObjectName("personelBilAd")
        self.personelBilSoyad = QtWidgets.QLabel(self.tab_5)
        self.personelBilSoyad.setGeometry(QtCore.QRect(240, 190, 151, 21))
        self.personelBilSoyad.setObjectName("personelBilSoyad")
        self.personelBilTelefon = QtWidgets.QLabel(self.tab_5)
        self.personelBilTelefon.setGeometry(QtCore.QRect(240, 220, 151, 21))
        self.personelBilTelefon.setObjectName("personelBilTelefon")
        self.personelBilMail = QtWidgets.QLabel(self.tab_5)
        self.personelBilMail.setGeometry(QtCore.QRect(240, 250, 191, 21))
        self.personelBilMail.setObjectName("personelBilMail")
        self.personelBilTip = QtWidgets.QLabel(self.tab_5)
        self.personelBilTip.setGeometry(QtCore.QRect(240, 280, 141, 21))
        self.personelBilTip.setObjectName("personelBilTip")
        self.personelBilMaas = QtWidgets.QLabel(self.tab_5)
        self.personelBilMaas.setGeometry(QtCore.QRect(240, 310, 141, 21))
        self.personelBilMaas.setObjectName("personelBilMaas")
        self.label_24 = QtWidgets.QLabel(self.tab_5)
        self.label_24.setGeometry(QtCore.QRect(668, 30, 131, 31))
        self.label_24.setObjectName("label_24")
        self.personelSilTC = QtWidgets.QLineEdit(self.tab_5)
        self.personelSilTC.setGeometry(QtCore.QRect(668, 70, 113, 31))
        self.personelSilTC.setObjectName("personelSilTC")
        self.personelSil = QtWidgets.QPushButton(self.tab_5)
        self.personelSil.setGeometry(QtCore.QRect(670, 130, 111, 28))
        self.personelSil.setObjectName("personelSil")
        self.personelUpTC = QtWidgets.QLineEdit(self.tab_5)
        self.personelUpTC.setGeometry(QtCore.QRect(480, 70, 113, 31))
        self.personelUpTC.setObjectName("personelUpTC")
        self.personelUpMail = QtWidgets.QLineEdit(self.tab_5)
        self.personelUpMail.setGeometry(QtCore.QRect(480, 170, 113, 31))
        self.personelUpMail.setObjectName("personelUpMail")
        self.personelUpTelefon = QtWidgets.QLineEdit(self.tab_5)
        self.personelUpTelefon.setGeometry(QtCore.QRect(480, 130, 113, 31))
        self.personelUpTelefon.setObjectName("personelUpTelefon")
        self.personelUpMaas = QtWidgets.QLineEdit(self.tab_5)
        self.personelUpMaas.setGeometry(QtCore.QRect(480, 250, 113, 31))
        self.personelUpMaas.setMaxLength(6)
        self.personelUpMaas.setObjectName("personelUpMaas")
        self.personelUpTip = QtWidgets.QLineEdit(self.tab_5)
        self.personelUpTip.setGeometry(QtCore.QRect(480, 210, 113, 31))
        self.personelUpTip.setObjectName("personelUpTip")
        self.personelGuncelle = QtWidgets.QPushButton(self.tab_5)
        self.personelGuncelle.setGeometry(QtCore.QRect(480, 310, 121, 28))
        self.personelGuncelle.setObjectName("personelGuncelle")
        self.personelSorgula = QtWidgets.QPushButton(self.tab_5)
        self.personelSorgula.setGeometry(QtCore.QRect(240, 120, 111, 28))
        self.personelSorgula.setObjectName("personelSorgula")
        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.label_7 = QtWidgets.QLabel(self.tab_6)
        self.label_7.setGeometry(QtCore.QRect(200, 30, 131, 31))
        self.label_7.setObjectName("label_7")
        self.label_6 = QtWidgets.QLabel(self.tab_6)
        self.label_6.setGeometry(QtCore.QRect(410, 30, 131, 31))
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(self.tab_6)
        self.label_5.setGeometry(QtCore.QRect(20, 30, 131, 31))
        self.label_5.setObjectName("label_5")
        self.marka = QtWidgets.QLineEdit(self.tab_6)
        self.marka.setGeometry(QtCore.QRect(20, 70, 113, 22))
        self.marka.setObjectName("marka")
        self.model = QtWidgets.QLineEdit(self.tab_6)
        self.model.setGeometry(QtCore.QRect(20, 110, 113, 22))
        self.model.setObjectName("model")
        self.koltukSayisi = QtWidgets.QLineEdit(self.tab_6)
        self.koltukSayisi.setGeometry(QtCore.QRect(20, 150, 113, 22))
        self.koltukSayisi.setObjectName("koltukSayisi")
        self.plaka = QtWidgets.QLineEdit(self.tab_6)
        self.plaka.setGeometry(QtCore.QRect(20, 190, 113, 22))
        self.plaka.setObjectName("plaka")
        self.otobusEkle = QtWidgets.QPushButton(self.tab_6)
        self.otobusEkle.setGeometry(QtCore.QRect(20, 240, 111, 31))
        self.otobusEkle.setObjectName("otobusEkle")
        self.plaka_2 = QtWidgets.QLineEdit(self.tab_6)
        self.plaka_2.setGeometry(QtCore.QRect(200, 70, 113, 22))
        self.plaka_2.setObjectName("plaka_2")
        self.bakimAciklama = QtWidgets.QTextEdit(self.tab_6)
        self.bakimAciklama.setGeometry(QtCore.QRect(200, 110, 111, 87))
        self.bakimAciklama.setObjectName("bakimAciklama")
        self.bakimaSok = QtWidgets.QPushButton(self.tab_6)
        self.bakimaSok.setGeometry(QtCore.QRect(200, 240, 111, 31))
        self.bakimaSok.setObjectName("bakimaSok")
        self.plaka_3 = QtWidgets.QLineEdit(self.tab_6)
        self.plaka_3.setGeometry(QtCore.QRect(380, 70, 113, 22))
        self.plaka_3.setObjectName("plaka_3")
        self.otobusSil = QtWidgets.QPushButton(self.tab_6)
        self.otobusSil.setGeometry(QtCore.QRect(380, 120, 111, 28))
        self.otobusSil.setObjectName("otobusSil")
        self.tabWidget_2.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.label_8 = QtWidgets.QLabel(self.tab_7)
        self.label_8.setGeometry(QtCore.QRect(140, 30, 131, 31))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab_7)
        self.label_9.setGeometry(QtCore.QRect(460, 30, 131, 31))
        self.label_9.setObjectName("label_9")
        self.indirimKodu_2 = QtWidgets.QLineEdit(self.tab_7)
        self.indirimKodu_2.setGeometry(QtCore.QRect(120, 80, 113, 22))
        self.indirimKodu_2.setObjectName("indirimKodu_2")
        self.indirimYuzdesi = QtWidgets.QLineEdit(self.tab_7)
        self.indirimYuzdesi.setGeometry(QtCore.QRect(120, 120, 113, 22))
        self.indirimYuzdesi.setObjectName("indirimYuzdesi")
        self.indirimSonTarih = QtWidgets.QDateTimeEdit(self.tab_7)
        self.indirimSonTarih.setGeometry(QtCore.QRect(90, 170, 194, 22))
        self.indirimSonTarih.setObjectName("indirimSonTarih")
        self.indirimEkle = QtWidgets.QPushButton(self.tab_7)
        self.indirimEkle.setGeometry(QtCore.QRect(100, 220, 161, 28))
        self.indirimEkle.setObjectName("indirimEkle")
        self.promosyonKodu = QtWidgets.QLineEdit(self.tab_7)
        self.promosyonKodu.setGeometry(QtCore.QRect(450, 80, 113, 22))
        self.promosyonKodu.setObjectName("promosyonKodu")
        self.promosyonYuzdesi = QtWidgets.QLineEdit(self.tab_7)
        self.promosyonYuzdesi.setGeometry(QtCore.QRect(450, 120, 113, 22))
        self.promosyonYuzdesi.setObjectName("promosyonYuzdesi")
        self.textEdit = QtWidgets.QTextEdit(self.tab_7)
        self.textEdit.setGeometry(QtCore.QRect(450, 170, 111, 87))
        self.textEdit.setObjectName("textEdit")
        self.promosyonEkle = QtWidgets.QPushButton(self.tab_7)
        self.promosyonEkle.setGeometry(QtCore.QRect(450, 280, 111, 28))
        self.promosyonEkle.setObjectName("promosyonEkle")
        self.tabWidget_2.addTab(self.tab_7, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.label_10 = QtWidgets.QLabel(self.tab_8)
        self.label_10.setGeometry(QtCore.QRect(70, 20, 131, 31))
        self.label_10.setObjectName("label_10")
        self.baslangic = QtWidgets.QDateTimeEdit(self.tab_8)
        self.baslangic.setGeometry(QtCore.QRect(70, 230, 194, 22))
        self.baslangic.setObjectName("baslangic")
        self.bitis = QtWidgets.QDateTimeEdit(self.tab_8)
        self.bitis.setGeometry(QtCore.QRect(70, 270, 194, 22))
        self.bitis.setObjectName("bitis")
        self.reklamBaslik = QtWidgets.QLineEdit(self.tab_8)
        self.reklamBaslik.setGeometry(QtCore.QRect(70, 70, 191, 22))
        self.reklamBaslik.setObjectName("reklamBaslik")
        self.reklamIcerik = QtWidgets.QTextEdit(self.tab_8)
        self.reklamIcerik.setGeometry(QtCore.QRect(70, 120, 191, 87))
        self.reklamIcerik.setObjectName("reklamIcerik")
        self.reklamEkle = QtWidgets.QPushButton(self.tab_8)
        self.reklamEkle.setGeometry(QtCore.QRect(70, 320, 191, 28))
        self.reklamEkle.setObjectName("reklamEkle")
        self.tabWidget_2.addTab(self.tab_8, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.label_13 = QtWidgets.QLabel(self.tab_9)
        self.label_13.setGeometry(QtCore.QRect(420, 30, 171, 31))
        self.label_13.setObjectName("label_13")
        self.label_12 = QtWidgets.QLabel(self.tab_9)
        self.label_12.setGeometry(QtCore.QRect(40, 30, 131, 31))
        self.label_12.setObjectName("label_12")
        self.kalkis = QtWidgets.QLineEdit(self.tab_9)
        self.kalkis.setGeometry(QtCore.QRect(30, 80, 113, 22))
        self.kalkis.setObjectName("kalkis")
        self.varis = QtWidgets.QLineEdit(self.tab_9)
        self.varis.setGeometry(QtCore.QRect(30, 120, 113, 22))
        self.varis.setObjectName("varis")
        self.kalkisTarihi = QtWidgets.QDateEdit(self.tab_9)
        self.kalkisTarihi.setGeometry(QtCore.QRect(30, 170, 194, 22))
        self.kalkisTarihi.setDateTime(QtCore.QDateTime(QtCore.QDate(2023, 12, 12), QtCore.QTime(0, 0, 0)))
        self.kalkisTarihi.setObjectName("kalkisTarihi")
        self.varisTarihi = QtWidgets.QDateEdit(self.tab_9)
        self.varisTarihi.setGeometry(QtCore.QRect(30, 220, 194, 22))
        self.varisTarihi.setDateTime(QtCore.QDateTime(QtCore.QDate(2023, 12, 13), QtCore.QTime(0, 0, 0)))
        self.varisTarihi.setObjectName("varisTarihi")
        self.seferOlustur = QtWidgets.QPushButton(self.tab_9)
        self.seferOlustur.setGeometry(QtCore.QRect(30, 280, 191, 28))
        self.seferOlustur.setObjectName("seferOlustur")
        self.fiyat = QtWidgets.QLineEdit(self.tab_9)
        self.fiyat.setGeometry(QtCore.QRect(420, 80, 113, 22))
        self.fiyat.setObjectName("fiyat")
        self.hareketSaati = QtWidgets.QTimeEdit(self.tab_9)
        self.hareketSaati.setGeometry(QtCore.QRect(420, 130, 118, 22))
        self.hareketSaati.setObjectName("hareketSaati")
        self.varisSaati = QtWidgets.QTimeEdit(self.tab_9)
        self.varisSaati.setGeometry(QtCore.QRect(420, 180, 118, 22))
        self.varisSaati.setObjectName("varisSaati")
        self.otobus = QtWidgets.QComboBox(self.tab_9)
        self.otobus.setGeometry(QtCore.QRect(420, 230, 171, 22))
        self.otobus.setObjectName("otobus")
        self.otobus.addItem("")
        self.sefer = QtWidgets.QComboBox(self.tab_9)
        self.sefer.setGeometry(QtCore.QRect(420, 280, 171, 22))
        self.sefer.setPlaceholderText("")
        self.sefer.setObjectName("sefer")
        self.sefer.addItem("")
        self.seferProgOlustur = QtWidgets.QPushButton(self.tab_9)
        self.seferProgOlustur.setGeometry(QtCore.QRect(420, 330, 171, 28))
        self.seferProgOlustur.setObjectName("seferProgOlustur")
        self.tabWidget_2.addTab(self.tab_9, "")
        self.tab_14 = QtWidgets.QWidget()
        self.tab_14.setObjectName("tab_14")
        self.sefereEkle = QtWidgets.QPushButton(self.tab_14)
        self.sefereEkle.setGeometry(QtCore.QRect(150, 200, 211, 41))
        self.sefereEkle.setObjectName("sefereEkle")
        self.calisanPrEkle = QtWidgets.QComboBox(self.tab_14)
        self.calisanPrEkle.setGeometry(QtCore.QRect(150, 50, 361, 31))
        self.calisanPrEkle.setObjectName("calisanPrEkle")
        self.calisanSefer = QtWidgets.QComboBox(self.tab_14)
        self.calisanSefer.setGeometry(QtCore.QRect(150, 130, 361, 31))
        self.calisanSefer.setObjectName("calisanSefer")
        self.label = QtWidgets.QLabel(self.tab_14)
        self.label.setGeometry(QtCore.QRect(150, 20, 141, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab_14)
        self.label_2.setGeometry(QtCore.QRect(150, 110, 141, 16))
        self.label_2.setObjectName("label_2")
        self.tabWidget_2.addTab(self.tab_14, "")
        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.tabWidget_2.addTab(self.tab_10, "")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget_3 = QtWidgets.QTabWidget(self.tab_4)
        self.tabWidget_3.setGeometry(QtCore.QRect(0, 10, 1021, 511))
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_11 = QtWidgets.QWidget()
        self.tab_11.setObjectName("tab_11")
        self.seferBilgileri = QtWidgets.QTableWidget(self.tab_11)
        self.seferBilgileri.setGeometry(QtCore.QRect(10, 50, 1001, 192))
        self.seferBilgileri.setObjectName("seferBilgileri")
        self.seferBilgileri.setColumnCount(8)
        self.seferBilgileri.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.seferBilgileri.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.seferBilgileri.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.seferBilgileri.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.seferBilgileri.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.seferBilgileri.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.seferBilgileri.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.seferBilgileri.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.seferBilgileri.setHorizontalHeaderItem(7, item)
        self.nereden = QtWidgets.QComboBox(self.tab_11)
        self.nereden.setGeometry(QtCore.QRect(10, 10, 141, 31))
        self.nereden.setObjectName("nereden")
        self.nereden.addItem("")
        self.nereye = QtWidgets.QComboBox(self.tab_11)
        self.nereye.setGeometry(QtCore.QRect(180, 10, 141, 31))
        self.nereye.setObjectName("nereye")
        self.nereye.addItem("")
        self.koltukSecimi = QtWidgets.QComboBox(self.tab_11)
        self.koltukSecimi.setGeometry(QtCore.QRect(270, 270, 141, 31))
        self.koltukSecimi.setObjectName("koltukSecimi")
        self.koltukSecimi.addItem("")
        self.nakit = QtWidgets.QRadioButton(self.tab_11)
        self.nakit.setGeometry(QtCore.QRect(460, 450, 95, 20))
        self.nakit.setObjectName("nakit")
        self.krediKarti = QtWidgets.QRadioButton(self.tab_11)
        self.krediKarti.setGeometry(QtCore.QRect(460, 420, 95, 20))
        self.krediKarti.setObjectName("krediKarti")
        self.label_16 = QtWidgets.QLabel(self.tab_11)
        self.label_16.setGeometry(QtCore.QRect(460, 390, 91, 21))
        self.label_16.setObjectName("label_16")
        self.biletOlustur = QtWidgets.QPushButton(self.tab_11)
        self.biletOlustur.setGeometry(QtCore.QRect(650, 270, 141, 41))
        self.biletOlustur.setObjectName("biletOlustur")
        self.indirimKodu = QtWidgets.QLineEdit(self.tab_11)
        self.indirimKodu.setGeometry(QtCore.QRect(460, 271, 141, 31))
        self.indirimKodu.setObjectName("indirimKodu")
        self.bileFiyat = QtWidgets.QLabel(self.tab_11)
        self.bileFiyat.setGeometry(QtCore.QRect(460, 350, 131, 21))
        self.bileFiyat.setObjectName("bileFiyat")
        self.musteriAd = QtWidgets.QLineEdit(self.tab_11)
        self.musteriAd.setGeometry(QtCore.QRect(100, 270, 113, 31))
        self.musteriAd.setObjectName("musteriAd")
        self.musteriSoyad = QtWidgets.QLineEdit(self.tab_11)
        self.musteriSoyad.setGeometry(QtCore.QRect(100, 310, 113, 31))
        self.musteriSoyad.setObjectName("musteriSoyad")
        self.musteriTC = QtWidgets.QLineEdit(self.tab_11)
        self.musteriTC.setGeometry(QtCore.QRect(100, 350, 113, 31))
        self.musteriTC.setObjectName("musteriTC")
        self.musteriTelefon = QtWidgets.QLineEdit(self.tab_11)
        self.musteriTelefon.setGeometry(QtCore.QRect(100, 390, 113, 31))
        self.musteriTelefon.setObjectName("musteriTelefon")
        self.musteriMail = QtWidgets.QLineEdit(self.tab_11)
        self.musteriMail.setGeometry(QtCore.QRect(100, 430, 113, 31))
        self.musteriMail.setObjectName("musteriMail")
        self.dateEdit = QtWidgets.QDateEdit(self.tab_11)
        self.dateEdit.setGeometry(QtCore.QRect(350, 11, 194, 31))
        self.dateEdit.setObjectName("dateEdit")
        self.biletAra = QtWidgets.QPushButton(self.tab_11)
        self.biletAra.setGeometry(QtCore.QRect(560, 10, 121, 31))
        self.biletAra.setObjectName("biletAra")
        self.indirimUygula = QtWidgets.QPushButton(self.tab_11)
        self.indirimUygula.setGeometry(QtCore.QRect(460, 310, 141, 28))
        self.indirimUygula.setObjectName("indirimUygula")
        self.tabWidget_3.addTab(self.tab_11, "")
        self.tab_12 = QtWidgets.QWidget()
        self.tab_12.setObjectName("tab_12")
        self.tcKimlikNo = QtWidgets.QLineEdit(self.tab_12)
        self.tcKimlikNo.setGeometry(QtCore.QRect(10, 20, 151, 31))
        self.tcKimlikNo.setMaxLength(11)
        self.tcKimlikNo.setObjectName("tcKimlikNo")
        self.biletBilgileri = QtWidgets.QTableWidget(self.tab_12)
        self.biletBilgileri.setGeometry(QtCore.QRect(10, 80, 1001, 192))
        self.biletBilgileri.setObjectName("biletBilgileri")
        self.biletBilgileri.setColumnCount(8)
        self.biletBilgileri.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.biletBilgileri.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.biletBilgileri.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.biletBilgileri.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.biletBilgileri.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.biletBilgileri.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.biletBilgileri.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.biletBilgileri.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.biletBilgileri.setHorizontalHeaderItem(7, item)
        self.sorgula = QtWidgets.QPushButton(self.tab_12)
        self.sorgula.setGeometry(QtCore.QRect(180, 20, 111, 31))
        self.sorgula.setObjectName("sorgula")
        self.iptalEt = QtWidgets.QPushButton(self.tab_12)
        self.iptalEt.setGeometry(QtCore.QRect(390, 300, 211, 51))
        self.iptalEt.setObjectName("iptalEt")
        self.tabWidget_3.addTab(self.tab_12, "")
        self.tabWidget.addTab(self.tab_4, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1052, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Personel Güncelle"))
        self.personelTelefon.setPlaceholderText(_translate("MainWindow", "Telefon Numarası"))
        self.personelSoyad.setPlaceholderText(_translate("MainWindow", "Soyad"))
        self.personelTC.setPlaceholderText(_translate("MainWindow", "T.C. Kimlik"))
        self.personelAd.setPlaceholderText(_translate("MainWindow", "Ad"))
        self.personelTip.setPlaceholderText(_translate("MainWindow", "Personel tipi"))
        self.personelEmail.setPlaceholderText(_translate("MainWindow", "e-mail"))
        self.personelMaas.setPlaceholderText(_translate("MainWindow", "Aylık Ücreti"))
        self.personelEkle.setText(_translate("MainWindow", "Personel Ekle"))
        self.label_11.setText(_translate("MainWindow", "Personel Ekleme"))
        self.label_17.setText(_translate("MainWindow", "Personel Sorgulama"))
        self.personelSor.setPlaceholderText(_translate("MainWindow", "T.C. Kimlik"))
        self.personelBilAd.setText(_translate("MainWindow", "Ad :"))
        self.personelBilSoyad.setText(_translate("MainWindow", "Soyad :"))
        self.personelBilTelefon.setText(_translate("MainWindow", "Telefon No:"))
        self.personelBilMail.setText(_translate("MainWindow", "e-mail"))
        self.personelBilTip.setText(_translate("MainWindow", "Personel Tipi : "))
        self.personelBilMaas.setText(_translate("MainWindow", "Aylık Ücreti : "))
        self.label_24.setText(_translate("MainWindow", "Personel Sil"))
        self.personelSilTC.setPlaceholderText(_translate("MainWindow", "T.C. Kimlik"))
        self.personelSil.setText(_translate("MainWindow", "SİL"))
        self.personelUpTC.setPlaceholderText(_translate("MainWindow", "T.C. Kimlik"))
        self.personelUpMail.setPlaceholderText(_translate("MainWindow", "e-mail"))
        self.personelUpTelefon.setPlaceholderText(_translate("MainWindow", "Telefon Numarası"))
        self.personelUpMaas.setPlaceholderText(_translate("MainWindow", "Aylık Ücreti"))
        self.personelUpTip.setPlaceholderText(_translate("MainWindow", "Personel tipi"))
        self.personelGuncelle.setText(_translate("MainWindow", "Güncelle"))
        self.personelSorgula.setText(_translate("MainWindow", "Sorgula"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("MainWindow", "Personel İşlemleri"))
        self.label_7.setText(_translate("MainWindow", "Otobus bakımı ekle"))
        self.label_6.setText(_translate("MainWindow", "Otobus Sil"))
        self.label_5.setText(_translate("MainWindow", "Otobus ekle"))
        self.marka.setPlaceholderText(_translate("MainWindow", "Marka"))
        self.model.setPlaceholderText(_translate("MainWindow", "Model"))
        self.koltukSayisi.setPlaceholderText(_translate("MainWindow", "Koltuk Sayısı"))
        self.plaka.setPlaceholderText(_translate("MainWindow", "Plaka"))
        self.otobusEkle.setText(_translate("MainWindow", "Otobüs Ekle"))
        self.plaka_2.setPlaceholderText(_translate("MainWindow", "Plaka"))
        self.bakimAciklama.setPlaceholderText(_translate("MainWindow", "Bakım açıklaması"))
        self.bakimaSok.setText(_translate("MainWindow", "Bakıma Sok"))
        self.plaka_3.setPlaceholderText(_translate("MainWindow", "Plaka"))
        self.otobusSil.setText(_translate("MainWindow", "Otobüs Sil"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), _translate("MainWindow", "Otobüs İşlemleri"))
        self.label_8.setText(_translate("MainWindow", "İndirim ekle"))
        self.label_9.setText(_translate("MainWindow", "Promosyon ekle"))
        self.indirimKodu_2.setPlaceholderText(_translate("MainWindow", "İndirim Kodu"))
        self.indirimYuzdesi.setPlaceholderText(_translate("MainWindow", "İndirim Yüzdesi"))
        self.indirimEkle.setText(_translate("MainWindow", "İndirim kuponu ekle"))
        self.promosyonKodu.setPlaceholderText(_translate("MainWindow", "Promosyon Kodu"))
        self.promosyonYuzdesi.setPlaceholderText(_translate("MainWindow", "Promosyon Yüzdesi"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "Promosyon açıklaması"))
        self.promosyonEkle.setText(_translate("MainWindow", "Promosyon Ekle"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), _translate("MainWindow", "İndirim ve Promosyon"))
        self.label_10.setText(_translate("MainWindow", "Reklam ekle"))
        self.reklamBaslik.setPlaceholderText(_translate("MainWindow", "Reklam başlığı"))
        self.reklamIcerik.setPlaceholderText(_translate("MainWindow", "Reklam içeriği"))
        self.reklamEkle.setText(_translate("MainWindow", "Reklam Ekle"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8), _translate("MainWindow", "Reklamlar"))
        self.label_13.setText(_translate("MainWindow", "Sefer programı oluştur"))
        self.label_12.setText(_translate("MainWindow", "Sefer oluştur"))
        self.kalkis.setPlaceholderText(_translate("MainWindow", "NEREDEN"))
        self.varis.setPlaceholderText(_translate("MainWindow", "NEREYE"))
        self.seferOlustur.setText(_translate("MainWindow", "Sefer Oluştur"))
        self.fiyat.setPlaceholderText(_translate("MainWindow", "Fiyat"))
        self.otobus.setItemText(0, _translate("MainWindow", "Otobus Seçin"))
        self.sefer.setItemText(0, _translate("MainWindow", "Sefer Seçin"))
        self.seferProgOlustur.setText(_translate("MainWindow", "Sefer Programı Oluştur"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_9), _translate("MainWindow", "Sefer İşlemleri"))
        self.sefereEkle.setText(_translate("MainWindow", "Sefere Ekle"))
        self.label.setText(_translate("MainWindow", "Personel Seç"))
        self.label_2.setText(_translate("MainWindow", "Sefer Seç"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_14), _translate("MainWindow", "Çalışan Programı"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_10), _translate("MainWindow", "Geri Bildirimler"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Şirket İşlemleri"))
        item = self.seferBilgileri.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Kalkış Yeri"))
        item = self.seferBilgileri.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Varış Yeri"))
        item = self.seferBilgileri.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Kalkış Tarihi"))
        item = self.seferBilgileri.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Varış Tarihi"))
        item = self.seferBilgileri.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Hareket Saati"))
        item = self.seferBilgileri.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Varış Saati"))
        item = self.seferBilgileri.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Otobüs"))
        item = self.seferBilgileri.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Fiyat"))
        self.nereden.setItemText(0, _translate("MainWindow", "NEREDEN"))
        self.nereye.setItemText(0, _translate("MainWindow", "NEREYE"))
        self.koltukSecimi.setItemText(0, _translate("MainWindow", "KOLTUK SEÇİMİ"))
        self.nakit.setText(_translate("MainWindow", "Nakit"))
        self.krediKarti.setText(_translate("MainWindow", "Kredi kartı"))
        self.label_16.setText(_translate("MainWindow", "Ödeme tipi"))
        self.biletOlustur.setText(_translate("MainWindow", "Bilet Oluştur"))
        self.indirimKodu.setPlaceholderText(_translate("MainWindow", "indirim kodunuz (opsiyonel)"))
        self.bileFiyat.setText(_translate("MainWindow", "Bilet Fiyatı :"))
        self.musteriAd.setPlaceholderText(_translate("MainWindow", "Ad"))
        self.musteriSoyad.setPlaceholderText(_translate("MainWindow", "Soyad"))
        self.musteriTC.setPlaceholderText(_translate("MainWindow", "T.C. Kimlik"))
        self.musteriTelefon.setPlaceholderText(_translate("MainWindow", "Telefon Numarası"))
        self.musteriMail.setPlaceholderText(_translate("MainWindow", "e-mail "))
        self.biletAra.setText(_translate("MainWindow", "Bilet Ara"))
        self.indirimUygula.setText(_translate("MainWindow", "İndirim Uygula"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_11), _translate("MainWindow", "Bilet Oluşturma"))
        self.tcKimlikNo.setPlaceholderText(_translate("MainWindow", "T.C. Kimlik numarası"))
        item = self.biletBilgileri.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Kalkış Yeri"))
        item = self.biletBilgileri.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Varış Yeri"))
        item = self.biletBilgileri.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Kalkış Tarihi"))
        item = self.biletBilgileri.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Varış Tarihi"))
        item = self.biletBilgileri.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Hareket Saati"))
        item = self.biletBilgileri.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Varış Saati"))
        item = self.biletBilgileri.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Koltuk No"))
        item = self.biletBilgileri.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Fiyat"))
        self.sorgula.setText(_translate("MainWindow", "Sorgula"))
        self.iptalEt.setText(_translate("MainWindow", "Seçili Bilet İptal Et"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_12), _translate("MainWindow", "Bilet Sorgulama ve İptal"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Müşteri İşlemleri"))
