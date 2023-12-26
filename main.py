import datetime
import sys

from PyQt5.QtWidgets import QMessageBox

from form import Ui_MainWindow
import psycopg2
from PyQt5 import QtWidgets, QtCore
from datetime import date

## 4 adet trigger oluştur
## rapor hazırla
## iş kuralları , varlık bağıntı diyagramı ve ilişkisel şema hazırla
## çalışan programı belirle
## iş kurallarını uygula




class firma(QtWidgets.QMainWindow):
    def __init__(self):
        super(firma, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.connection = psycopg2.connect(host="localhost", port="5432", database="otobusFirmasi", user="postgres",
                                      password="elsat")
        self.crsr = self.connection.cursor()
        self.crsr.execute("SELECT version()")
        db_version = self.crsr.fetchone()
        print(db_version)

        self.calisanVeSeferGetir()
        self.ui.personelEkle.clicked.connect(self.eklePersonel)
        self.ui.personelSil.clicked.connect(self.silPersonel)
        self.ui.personelSorgula.clicked.connect(self.sorgulaPersonel)
        self.ui.personelGuncelle.clicked.connect(self.guncellePersonel)

        self.ui.otobusEkle.clicked.connect(self.ekleOtobus)
        self.ui.otobusSil.clicked.connect(self.silOtobus)
        self.ui.bakimaSok.clicked.connect(self.bakimOtobus)

        self.ui.indirimEkle.clicked.connect(self.ekleIndirim)
        self.ui.promosyonEkle.clicked.connect(self.eklePromosyon)

        self.ui.reklamEkle.clicked.connect(self.ekleReklam)

        self.ui.seferOlustur.clicked.connect(self.seferOlustur)
        self.ui.seferProgOlustur.clicked.connect(self.seferProgramOlustur)

        self.ui.biletOlustur.clicked.connect(self.olusturBilet)
        self.ui.sorgula.clicked.connect(self.sorgulaBilet)
        self.ui.iptalEt.clicked.connect(self.iptalBilet)

        self.ui.seferBilgileri.itemSelectionChanged.connect(self.selection_changed)
        self.ui.indirimUygula.clicked.connect(self.indirimUygula)

        self.ui.sefereEkle.clicked.connect(self.calisanPrOlustur)

        self.ui.biletAra.clicked.connect(self.listeleBilet)
        self.otobusVeSeferListele()
        self.neredenNereyeListele()

    def otobusVeSeferListele(self):
        query = """SELECT "Plaka" FROM "Otobus" """
        self.crsr.execute(query)
        results = self.crsr.fetchall()
        # self.ui.otobus.addItems(results)
        for i in results:
            all_items = [self.ui.otobus.itemText(i) for i in range(self.ui.otobus.count())]
            if i[0] in all_items:
                pass
            else:
                self.ui.otobus.addItem(i[0])

        self.crsr.execute("ROLLBACK")

        query = """SELECT "Kalkıs","Varıs","KalkısTarih" FROM "Sefer" """
        self.crsr.execute(query)

        results2 = self.crsr.fetchall()

        for j in results2:
            all_items = [self.ui.sefer.itemText(i) for i in range(self.ui.sefer.count())]
            if f"{j[0]}-{j[1]}-{j[2]}" in all_items:
                pass
            else:
                self.ui.sefer.addItem(f"{j[0]}-{j[1]}-{j[2]}")

    def neredenNereyeListele(self):
        query = """SELECT "Kalkıs","Varıs" FROM "Sefer" """
        self.crsr.execute(query)

        results2 = self.crsr.fetchall()

        for j in results2:
            all_items = [self.ui.nereden.itemText(i) for i in range(self.ui.nereden.count())]
            if f"{j[0]}" in all_items:
                pass
            else:
                self.ui.nereden.addItem(f"{j[0]}")

        for k in results2:
            all_items = [self.ui.nereye.itemText(i) for i in range(self.ui.nereye.count())]
            if f"{k[1]}" in all_items:
                pass
            else:
                self.ui.nereye.addItem(f"{k[1]}")

    def eklePersonel(self):
        ad = self.ui.personelAd.text()
        soyad = self.ui.personelSoyad.text()
        tc = int(self.ui.personelTC.text())
        telefon = self.ui.personelTelefon.text()
        email = self.ui.personelEmail.text()
        tip = self.ui.personelTip.text()
        maas = int(self.ui.personelMaas.text())
        tarih = str(date.today())

        # Fonksiyonu çağırma
        query = f"""SELECT "Personel"."manOlusturPersonel"('{ad}','{soyad}','{email}','{tarih}',{maas},'{telefon}','{tip}',{tc});"""
        print("\n"+query+"\n")
        try:
            self.crsr.execute(query)
            self.connection.commit()
            QMessageBox.information(self,"Başarılı","Personel başarıyla oluşturuldu.")
        except Exception as e:
            print(e)
        self.crsr.execute("ROLLBACK")

    def silPersonel(self):
        tc = int(self.ui.personelSilTC.text())
        query = f"""CALL "Personel"."silPersonel"({tc})"""
        try:
            self.crsr.execute(query)
            self.connection.commit()
            QMessageBox.information(self,"Başarılı","Personel başarıyla silindi.")
        except:
            pass

        self.crsr.execute("ROLLBACK")

    def sorgulaPersonel(self):
        tc_kimlik = self.ui.personelSor.text()
        try:
            query = f"""SELECT * FROM "Personel"."Personel" WHERE "tcKimlik" = {tc_kimlik};"""
            self.crsr.execute(query)
            result = self.crsr.fetchone()
            self.ui.personelBilAd.setText(f"Ad: {result[1]}")
            self.ui.personelBilSoyad.setText(f"Soyad: {result[2]}")
            self.ui.personelBilMaas.setText(f"Aylık Ücreti: {result[3]}")
            self.ui.personelBilTelefon.setText(f"Telefon No: {result[4]}")
            self.ui.personelBilMail.setText(f"e-mail: {result[5]}")
            self.ui.personelBilTip.setText(f"Personel Tipi: {result[6]}")

        except Exception as e:
            print(e)
            self.ui.personelBilAd.setText(f"Ad:")
            self.ui.personelBilSoyad.setText(f"Soyad:")
            self.ui.personelBilMaas.setText(f"Aylık Ücreti:")
            self.ui.personelBilTelefon.setText(f"Telefon No:")
            self.ui.personelBilMail.setText(f"e-mail:")
            self.ui.personelBilTip.setText(f"Personel Tipi:")

        self.crsr.execute("ROLLBACK")

    def guncellePersonel(self):

        try:
            phone = self.ui.personelUpTelefon.text()
            email = self.ui.personelUpMail.text()
            tip = self.ui.personelUpTip.text()
            maas = self.ui.personelUpMaas.text()
            tc = self.ui.personelUpTC.text()

            query = f"""SELECT * FROM "Personel"."Personel" WHERE "tcKimlik" = {tc};"""
            self.crsr.execute(query)
            result = self.crsr.fetchone()

            query = f"""UPDATE "Personel"."Personel" SET "phoneNumber"={phone},"email"='{email}',"personelTipi"='{tip}',maas={maas} WHERE "tcKimlik"={tc}"""
            self.crsr.execute(query)
            self.crsr.execute("ROLLBACK")
            QMessageBox.information(self,"Başarılı","Personel başarıyla güncellendi")

            if tip == "D":
                query = f"""INSERT INTO "Personel"."Driver" ("personelNo", "sirket") VALUES ({result[0]},'Mirdes Tic. Ltd. Şti.');"""

                query2 = f"""DELETE FROM "Personel"."vasifsizPer" WHERE "personelNo" = {result[0]};"""

                self.crsr.execute(query2)
                self.connection.commit()

            else:
                query2 = f"""INSERT INTO "Personel"."vasifsizPer" ("personelNo", "sirket") VALUES ({result[0]},'Mirdes Tic. Ltd. Şti.');"""
                self.crsr.execute(query2)
                self.connection.commit()

                query = f"""DELETE FROM "Personel"."Driver" WHERE "personelNo" = {result[0]};"""
            self.crsr.execute(query)

            self.connection.commit()

        except Exception as e:
            print(e)

        self.crsr.execute("ROLLBACK")

    def ekleOtobus(self):
        marka = self.ui.marka.text()
        model = self.ui.model.text()
        koltukSay = int(self.ui.koltukSayisi.text())
        plaka = self.ui.plaka.text()
        try:
            query = f"""SELECT "public"."olusturotobus"({koltukSay},'{marka}','{model}','{plaka}'); """

            self.crsr.execute(query)
            self.connection.commit()
            QMessageBox.information(self,"Başarılı","Otobüs başarıyla kaydedildi")
        except Exception as e:
            QMessageBox.warning(self,"Başarısız","Otobüs zaten kayıtlı")
            print(e)

        self.otobusVeSeferListele()
        self.crsr.execute("ROLLBACK")

    def silOtobus(self):
        plaka = self.ui.plaka_3.text()
        query = f"""DELETE FROM "public"."Otobus" WHERE "Plaka"='{plaka}';"""
        try:
            self.crsr.execute(query)
            self.connection.commit()
            QMessageBox.information(self,"Başarılı","Otobüs başarıyla silindi")
        except Exception as e:
            print(e)
            QMessageBox.warning(self,"HATA","Otobüs bulunamadı")

        self.crsr.execute("ROLLBACK")

    def bakimOtobus(self):
        plaka = self.ui.plaka_2.text()
        aciklama = self.ui.bakimAciklama.toPlainText()

        query = f"""SELECT "BusID" FROM "Otobus" WHERE "Plaka" = '{plaka}';"""

        self.crsr.execute(query)
        result = self.crsr.fetchone()[0]
        print(result)
        tarih = str(date.today())

        try:
            query_bakim = f"""INSERT INTO "otobusBakim"("busID","bakimTarihi",aciklama) VALUES({result},'{tarih}','{aciklama}'); """
            self.crsr.execute(query_bakim)
            self.connection.commit()
            self.crsr.execute("ROLLBACK")
            QMessageBox.information(self, "Başarılı", "Otobüs bakımı oluşturuldu.")

        except Exception as e:
            print(e)

    def ekleIndirim(self):
        indirimKod = self.ui.indirimKodu_2.text()
        indirimYuzde = int(self.ui.indirimYuzdesi.text())
        indirimTarih = self.ui.indirimSonTarih.dateTime().toString("yyyy-MM-dd HH:mm:ss")

        try:
            query = f"""INSERT INTO "indirim"("indirimKodu","indirimYuzdesi","sonKullanmaTarihi") VALUES('{indirimKod}',{indirimYuzde},'{indirimTarih}');"""
            self.crsr.execute(query)
            self.connection.commit()
            self.crsr.execute("ROLLBACK")
            QMessageBox.information(self,"Başarılı","İndirim kuponu başarıyla kaydedildi.")

        except Exception as e:
            print(e)

    def eklePromosyon(self):
        promoKod = self.ui.promosyonKodu.text()
        promoYuzde = self.ui.promosyonYuzdesi.text()
        promoAciklama = self.ui.textEdit.toPlainText()

        try:
            query = f"""INSERT INTO "Promosyon"("promoKodu","promosyonYuzdesi","tanim") VALUES('{promoKod}',{promoYuzde},'{promoAciklama}');"""
            self.crsr.execute(query)
            self.connection.commit()
            self.crsr.execute("ROLLBACK")
            QMessageBox.information(self, "Başarılı", "Promosyon kuponu başarıyla kaydedildi.")

        except Exception as e:
            print(e)

    def ekleReklam(self):
        reklamBas = self.ui.reklamBaslik.text()
        reklamDetay = self.ui.reklamIcerik.toPlainText()
        reklamBaslangıc = self.ui.baslangic.dateTime().toString("yyyy-MM-dd HH:mm:ss")
        reklamBitis = self.ui.bitis.dateTime().toString("yyyy-MM-dd HH:mm:ss")

        try:
            query = f"""INSERT INTO "Reklam"("reklamBaslik","reklamIcerigi","baslangıcTarihi","bitisTarihi") VALUES('{reklamBas}','{reklamDetay}','{reklamBaslangıc}','{reklamBitis}');"""
            self.crsr.execute(query)
            self.connection.commit()
            self.crsr.execute("ROLLBACK")
            QMessageBox.information(self, "Başarılı", "Reklam başarıyla kaydedildi.")
        except Exception as e:
            print(e)

    def seferOlustur(self):
        kalkis = self.ui.kalkis.text()
        varis = self.ui.varis.text()
        kalkisTarih = self.ui.kalkisTarihi.dateTime().toString("yyyy-MM-dd")
        varisTaarih = self.ui.varisTarihi.dateTime().toString("yyyy-MM-dd")

        try:
            query = f"""INSERT INTO "Sefer"("Kalkıs","Varıs","KalkısTarih","VarisTarihi") VALUES('{kalkis}','{varis}','{kalkisTarih}','{varisTaarih}');"""
            self.crsr.execute(query)
            self.connection.commit()
            self.otobusVeSeferListele()
            self.crsr.execute("ROLLBACK")
            QMessageBox.information(self, "Başarılı", "Sefer başarıyla kaydedildi.")

        except Exception as e:
            print(e)

    def seferProgramOlustur(self):
        fiat = self.ui.fiyat.text()
        kalkis = self.ui.hareketSaati.dateTime().toString("HH:mm")
        varis = self.ui.varisSaati.dateTime().toString("HH:mm")

        ## otobus seç
        plaka = self.ui.otobus.currentText()
        sefer = self.ui.sefer.currentText()

        try:
            query = f"""SELECT "BusID" FROM "Otobus" WHERE "Plaka"='{plaka}'"""
            self.crsr.execute(query)
            result = self.crsr.fetchone()

            kalk = sefer.split("-")[0]
            var = sefer.split("-")[1]
            hareketTarih = sefer.split("-")[2]+"-"+sefer.split("-")[3]+"-"+sefer.split("-")[4]

            query = f"""SELECT "SeferID" FROM "Sefer" WHERE "Kalkıs"='{kalk}' AND "Varıs"='{var}' AND "KalkısTarih"='{hareketTarih}' """
            self.crsr.execute(query)
            result2 = self.crsr.fetchone()

            otobusID = result[0]
            seferID = result2[0]

            query = f"""INSERT INTO "SeferProgrami"("sefer","otobus","hareketSaati","varisSaati","Fiyat") VALUES({seferID},{otobusID},'{kalkis}','{varis}',{fiat});"""
            self.crsr.execute(query)
            self.connection.commit()
            QMessageBox.information(self,"Başarılı","Sefer programı başarıyla oluşturuldu.")
            self.crsr.execute("ROLLBACK")

        except Exception as e:
            QMessageBox.warning(self,"Başarısız","Bu otobus aynı saatte aynı sefer için kullanılıyor-")
            print(e)

        self.neredenNereyeListele()

    def listeleBilet(self):

        total_rows = self.ui.seferBilgileri.rowCount()

        # Tüm satırları silin
        for row in range(total_rows - 1, -1, -1):
            self.ui.seferBilgileri.removeRow(row)

        self.ui.koltukSecimi.clear()
        self.ui.koltukSecimi.addItem("KOLTUK SEÇİMİ")

        nereden = self.ui.nereden.currentText()
        nereye = self.ui.nereye.currentText()
        try:
            tarih = self.ui.dateEdit.dateTime().toString("yyyy-MM-dd")
        except Exception as e:
            print(e)

        try:
            query = f"""SELECT * FROM "Sefer" """
            self.crsr.execute(query)
            result = self.crsr.fetchall()
            setrow = 0
            for i in result:
                seferID = i[0]
                if i[1] == nereden and i[2] == nereye and f"{i[3]}" == f"{tarih}":

                    query = f"""SELECT * FROM "SeferProgrami" """
                    self.crsr.execute(query)
                    result3 = self.crsr.fetchall()
                    row2 = 0
                    print(result3)

                    for j in result3:
                        if j[1] == seferID:
                            otobusID = j[2]
                            query = f"""SELECT "Plaka" FROM "Otobus" WHERE "BusID"='{otobusID}'"""
                            self.crsr.execute(query)
                            plaka = self.crsr.fetchone()

                            hareketSaat = j[3]
                            varisSaat = j[4]
                            fiyat = j[5]
                            self.ui.seferBilgileri.insertRow(setrow)

                            self.ui.seferBilgileri.setItem(row2, 0, QtWidgets.QTableWidgetItem(f"{i[1]}"))
                            self.ui.seferBilgileri.setItem(row2, 1, QtWidgets.QTableWidgetItem(f"{i[2]}"))
                            self.ui.seferBilgileri.setItem(row2, 2, QtWidgets.QTableWidgetItem(f"{i[3]}"))
                            self.ui.seferBilgileri.setItem(row2, 3, QtWidgets.QTableWidgetItem(f"{i[4]}"))
                            self.ui.seferBilgileri.setItem(row2, 4, QtWidgets.QTableWidgetItem(f"{hareketSaat}"))
                            self.ui.seferBilgileri.setItem(row2, 5, QtWidgets.QTableWidgetItem(f"{varisSaat}"))
                            self.ui.seferBilgileri.setItem(row2, 6, QtWidgets.QTableWidgetItem(f"{plaka[0]}"))
                            self.ui.seferBilgileri.setItem(row2, 7, QtWidgets.QTableWidgetItem(f"{fiyat}"))

                            row2 += 1
                            setrow += 1

        except Exception as e:
            print(e)

    def indirimUygula(self):

        indirimKodu = self.ui.indirimKodu.text()
        try:
            query = f"""SELECT "indirimYuzdesi" FROM "indirim" WHERE "indirimKodu"='{indirimKodu}' """
            self.crsr.execute(query)
            result = self.crsr.fetchone()
            indirimYuzdesi = result[0]

            if result:

                selected_row = self.ui.seferBilgileri.currentRow()

                # Seçili sütunlardaki verileri alın
                selected_data = [self.ui.seferBilgileri.item(selected_row, col).text() for col in
                                 range(self.ui.seferBilgileri.columnCount())]

                fiyat = selected_data[7]

                newFiyat = int(fiyat)*int(indirimYuzdesi)/100
                self.newFiyat = int(fiyat)-newFiyat

                self.ui.bileFiyat.setText(f"Bilet Fiyatı: {self.newFiyat}")
                QMessageBox.information(self,"Başarılı","İndirim uygulandı")

            else:
                QMessageBox.warning(self,"Bulunamadı","Böyle bir indirim kodu bulunmamaktadır.")
        except Exception as e:
            print(e)

    def selection_changed(self):
        try:
            selected_row = self.ui.seferBilgileri.currentRow()

            # Seçili sütunlardaki verileri alın
            selected_data = [self.ui.seferBilgileri.item(selected_row, col).text() for col in range(self.ui.seferBilgileri.columnCount())]

            print(f"Seçili Satır: {selected_row}")
            print("Seçili Sütun Verileri:", selected_data)

            kalkisSaat = selected_data[4]
            varisSaat = selected_data[5]

            query = f"""SELECT "seferProgramID" FROM "SeferProgrami" WHERE "hareketSaati"='{kalkisSaat}' AND "varisSaati"='{varisSaat}'"""
            self.crsr.execute(query)
            self.seferID = int(self.crsr.fetchone()[0])

            otobusPlaka = selected_data[6]
            self.newFiyat = selected_data[7]

            query = f"""SELECT "koltukSayisi" FROM "Otobus" WHERE "Plaka"='{otobusPlaka}' """
            self.crsr.execute(query)
            koltukSay = int(self.crsr.fetchone()[0])

            self.ui.bileFiyat.setText(f"Bilet Fiyatı: {self.newFiyat} TL")

            self.ui.koltukSecimi.clear()
            for i in range(1,koltukSay+1):
                self.ui.koltukSecimi.addItem(str(i))

        except Exception as e:
            print(e)

    def olusturBilet(self):
        try:
            musteriAd = self.ui.musteriAd.text()
            musteriSoyad = self.ui.musteriSoyad.text()
            musteriTC = int(self.ui.musteriTC.text())
            musteriTel = int(self.ui.musteriTelefon.text())
            musteriMail = self.ui.musteriMail.text()
        except:
            pass
        try:
            result = None
            try:
                query = f"""SELECT * FROM "Musteri" WHERE "tcKimlik"={musteriTC}"""
                self.crsr.execute(query)
                result = self.crsr.fetchone()
            except:
                pass

            if result:
                pass
            else:
                query = f"""INSERT INTO "Musteri"("adi","soyadi","phoneNumber","email","tcKimlik") VALUES('{musteriAd}','{musteriSoyad}',{musteriTel},'{musteriMail}',{musteriTC}); """
                self.crsr.execute(query)
                self.connection.commit()
                self.crsr.execute("ROLLBACK")

            koltuk = self.ui.koltukSecimi.currentText()
            query = f"""SELECT "CustomerID" FROM "Musteri" WHERE "tcKimlik"={musteriTC} """
            self.crsr.execute(query)
            result = self.crsr.fetchone()
            print(result)
            musteriID = int(result[0])
            an = datetime.datetime.now()
            satinAlmaTarih = datetime.datetime.strftime(an, '%Y-%m-%d')


            query = f"""SELECT * FROM "Bilet" WHERE "seferPrID"={self.seferID} AND "koltukNO"={koltuk} """
            self.crsr.execute(query)
            result = self.crsr.fetchone()
            print(result)
            if result:
                QMessageBox.warning(self,"DOLU","Seçilen koltuk dolu")
            else:
                odemeTip = None
                for i in range(1, 2):
                    buttonname = self.ui.krediKarti.isChecked()
                    buttonname2 = self.ui.nakit.isChecked()

                    if buttonname:
                        odemeTip = "Kredi Kartı"

                    elif buttonname2:
                        odemeTip = "Nakit"
                    else:
                        odemeTip = None

                if odemeTip:
                    try:
                        query = f"""INSERT INTO "Bilet"("customerID","fiyat","koltukNO","SatinalmaTarihi","seferPrID") VALUES({musteriID},{self.newFiyat},{koltuk},'{satinAlmaTarih}',{self.seferID});"""
                        self.crsr.execute(query)
                        self.connection.commit()

                        self.crsr.execute("ROLLBACK")
                        query = f"""SELECT "TicketID" FROM "Bilet" WHERE "koltukNO"={koltuk} AND "seferPrID"={self.seferID} AND "customerID"={musteriID} """
                        self.crsr.execute(query)
                        result = self.crsr.fetchone()

                        query = f"""INSERT INTO "Odeme"("ticketID","odemeTarihi","odemeTipi") VALUES({result[0]},'{satinAlmaTarih}','{odemeTip}'); """
                        self.crsr.execute(query)
                        self.connection.commit()
                        QMessageBox.information(self,"Başarılı","Bilet başarıyla oluşturuldu.")
                        self.crsr.execute("ROLLBACK")
                    except:
                        QMessageBox.warning(self,"Başarısız","Müşteri bu seferde zaten bilet almış.")

                else:
                    QMessageBox.warning(self,"Uyarı","Ödeme tip seçin")

        except Exception as e:
            print(e)

    def sorgulaBilet(self):
        tcKimlik = self.ui.tcKimlikNo.text()

        total_rows = self.ui.biletBilgileri.rowCount()

        # Tüm satırları silin
        for row in range(total_rows - 1, -1, -1):
            self.ui.biletBilgileri.removeRow(row)


        try:
            query = f"""SELECT "CustomerID" FROM "Musteri" WHERE "tcKimlik"={tcKimlik} """
            self.crsr.execute(query)
            result = self.crsr.fetchone()

            customerID = int(result[0])

            query = f"""SELECT * FROM "Bilet" WHERE "customerID"={customerID} """
            self.crsr.execute(query)
            result1 = self.crsr.fetchall()
            setrow = 0
            row2 = 0

            for i in result1:
                seferPrId = i[2]
                koltukNo = i[3]
                fiyat = i[4]

                query = f"""SELECT "sefer","hareketSaati","varisSaati" FROM "SeferProgrami" WHERE "seferProgramID"={seferPrId} """
                self.crsr.execute(query)
                result = self.crsr.fetchone()
                sefer = result[0]
                hareketSaat = result[1]
                varisSaat = result[2]

                query = f"""SELECT * FROM "Sefer" WHERE "SeferID"={sefer} """
                self.crsr.execute(query)
                result2 = self.crsr.fetchone()
                kalkisYer = result2[1]
                varisYer = result2[2]
                kalkisTar = result2[3]
                varisTarih = result2[4]

                self.ui.biletBilgileri.insertRow(setrow)

                self.ui.biletBilgileri.setItem(row2, 0, QtWidgets.QTableWidgetItem(f"{kalkisYer}"))
                self.ui.biletBilgileri.setItem(row2, 1, QtWidgets.QTableWidgetItem(f"{varisYer}"))
                self.ui.biletBilgileri.setItem(row2, 2, QtWidgets.QTableWidgetItem(f"{kalkisTar}"))
                self.ui.biletBilgileri.setItem(row2, 3, QtWidgets.QTableWidgetItem(f"{varisTarih}"))
                self.ui.biletBilgileri.setItem(row2, 4, QtWidgets.QTableWidgetItem(f"{hareketSaat}"))
                self.ui.biletBilgileri.setItem(row2, 5, QtWidgets.QTableWidgetItem(f"{varisSaat}"))
                self.ui.biletBilgileri.setItem(row2, 6, QtWidgets.QTableWidgetItem(f"{koltukNo}"))
                self.ui.biletBilgileri.setItem(row2, 7, QtWidgets.QTableWidgetItem(f"{fiyat}"))

                row2 += 1
                setrow += 1

        except Exception as e:
            print(e)

    def iptalBilet(self):
        try:
            tcKimlik = self.ui.tcKimlikNo.text()

            selected_row = self.ui.biletBilgileri.currentRow()

            # Seçili sütunlardaki verileri alın
            selected_data = [self.ui.biletBilgileri.item(selected_row, col).text() for col in
                             range(self.ui.biletBilgileri.columnCount())]

            print(f"Seçili Satır: {selected_row}")
            print("Seçili Sütun Verileri:", selected_data)

            ###
            query = f"""SELECT "CustomerID" FROM "Musteri" WHERE "tcKimlik"={tcKimlik} """
            self.crsr.execute(query)
            result = self.crsr.fetchone()
            print(result)
            customerID = int(result[0])
            koltukNo = int(selected_data[6])
            kalkis = selected_data[0]
            varis = selected_data[1]
            kalkTarih = selected_data[2]
            varTarih = selected_data[3]
            kalkisSaat = selected_data[4]
            varisSaat = selected_data[5]

            print(customerID,koltukNo,kalkis,varis,kalkTarih,varTarih,kalkisSaat,varisSaat)

            query = f"""SELECT "SeferID" FROM "Sefer" WHERE "Kalkıs"='{kalkis}' AND "Varıs"='{varis}' AND "KalkısTarih"='{kalkTarih}' AND "VarisTarihi"='{varTarih}' """
            self.crsr.execute(query)
            seferID = int(self.crsr.fetchone()[0])
            print(seferID)

            query = f"""SELECT "seferProgramID" FROM "SeferProgrami" WHERE "sefer"={seferID} AND "hareketSaati"='{kalkisSaat}' AND "varisSaati"='{varisSaat}' """
            self.crsr.execute(query)
            seferPrID = int(self.crsr.fetchone()[0])
            print(seferPrID)

            query = f"""DELETE FROM "Bilet" WHERE "customerID"={customerID} AND "seferPrID"={seferPrID} AND "koltukNO"={koltukNo} """
            self.crsr.execute(query)
            self.connection.commit()

            QMessageBox.information(self,"Başarılı","Bilet başarıyla silindi.")
            self.sorgulaBilet()
            self.crsr.execute("ROLLBACK")

        except Exception as e:
            print(e)


    def calisanVeSeferGetir(self):
        query = f"""SELECT "tcKimlik","adi","soyadi" FROM "Personel"."Personel" """
        self.crsr.execute(query)

        results = self.crsr.fetchall()

        for i in results:
            item = f"{i[0]}-{i[1]}-{i[2]}"
            self.ui.calisanPrEkle.addItem(item)

        query = f"""SELECT "sefer","hareketSaati" FROM "SeferProgrami" """
        self.crsr.execute(query)
        result = self.crsr.fetchall()

        for i in result:
            item2 = f"""SELECT "Kalkıs","Varıs","KalkısTarih" FROM "Sefer" WHERE "SeferID"={i[0]} """
            self.crsr.execute(item2)
            res = self.crsr.fetchone()

            addSefer = f"{res[0]}-{res[1]}-{res[2]}-{i[1]}"

            self.ui.calisanSefer.addItem(addSefer)


    def calisanPrOlustur(self):
        calisan = self.ui.calisanPrEkle.currentText()
        sefer = self.ui.calisanSefer.currentText()

        tcKimlik = calisan.split("-")[0]
        seferKalkis = sefer.split("-")[0]
        seferVaris = sefer.split("-")[1]
        seferTarih = f"{sefer.split('-')[2]}-{sefer.split('-')[3]}-{sefer.split('-')[4]}"
        hareketSaati = f"{sefer.split('-')[5]}"


        query = f"""SELECT "SeferID" FROM "Sefer" WHERE "Kalkıs"='{seferKalkis}' AND "Varıs"='{seferVaris}' AND "KalkısTarih"='{seferTarih}' """
        self.crsr.execute(query)
        seferID = self.crsr.fetchone()
        print(seferID)


        query = f"""SELECT "seferProgramID" FROM "SeferProgrami" WHERE "sefer"={int(seferID[0])} AND "hareketSaati"='{hareketSaati}' """
        self.crsr.execute(query)
        seferPrID = self.crsr.fetchone()
        print("\nsefer programi ıd: ",seferPrID)

        query = f"""SELECT "personelNo" FROM "Personel"."Personel" WHERE "tcKimlik"={tcKimlik} """
        self.crsr.execute(query)
        customerID = self.crsr.fetchone()
        print(customerID)

        try:
            query = f"""INSERT INTO "calisanProgrami"("calisan","seferProgrami") VALUES({int(customerID[0])},{int(seferPrID[0])});"""
            self.crsr.execute(query)
            self.connection.commit()
            QMessageBox.information(self,"Başarılı","Çalışan sefer programına görevlendirilmiştir.")
        except Exception as e:
            QMessageBox.warning(self,"Başarısız","Çalışan zaten sefer programında görevli.")

            print(e)

def run():
    ap = QtWidgets.QApplication(sys.argv)
    win = firma()
    win.show()
    sys.exit(ap.exec_())

if __name__ == "__main__":
    run()