#Lárus Óskar Lárusson
#FOR1TÖ05BD
#2017
#Lokaverkefni


import random


byrjun=0
while byrjun==0:# Valmynd
    print()
    print("-------HANGMAN-------")
    print("1. Nöfn")
    print("2. Dýr")
    print("3. Lönd")
    print("4. Hætta")
    val=int(input("Veldu lið 1-4: "))
    print("")

    orð = []# Tómur listi búinn til
    class Hengimann: #Klasinn Hengimann
        def __init__(self, orð):
            self.orð = orð
            self.svar = orð[random.randint(0, len(orð) - 1)]
            self.gisk = {}


        def giska(self,stafur):# fallið giska sem heldur utan um stafinn sem þú giskar á
            stafur = gisk.lower()
            if stafur in self.gisk:
                print("þú ert búinn að giska á þennan staf!!!!")
            elif len(stafur) !=1:
                print("Sláðu inn einn staf í einu!!!!")
            elif stafur not in  'aábcdðeéfghiíjklmnoópqrstuúvxyýzþæö':
                print("Sláðu inn bókstaf!!!!")
            else:
                self.gisk[stafur] = True

        def prenta_gisk(self):# fall sem prentar út stafinn sem ú giskaðir á
            print("Þú hefur giskað á:", end=" ")
            for gisk in self.gisk:
                print(gisk, end=" ")
            print()

        def prenta_orð_falið(self):
            for stafur in self.svar:
                if stafur in self.gisk: # setja _ í staðin fyrir orðið en ef þú getur réttan staf þá kemur hann í staðinn
                    print(stafur, end=" ")
                else:
                    print("_", end=" ")
            print()

        def sigur(self):
            for stafur in self.svar:
                if stafur not in self.gisk:
                    return False
            return True

        def tap(self): # fall sem passar að þú getir ekki giskað vitlaust nema 6 sinnum
            vitlaus_gisk = 0
            for gisk in self.gisk:
                if gisk not in self.svar:
                    vitlaus_gisk += 1
            return vitlaus_gisk > 5


        def buinn(self):
            return self.tap() or self.sigur()


        def spilaaftur():#fall sem segir til hvort þú viljir spila leikinn áfram eða ekki
            print()
            print("Viltu spila aftur? (Já eða Nei)")
            return input().lower().startswith('j')


    Leikur_buinn = False
    staða = [0, 0]
    if val == 1: # ef valið er 1 í valmynd
        print("Þú hefur valið að giska á nöfn í Hangman")
        print("Þú tapar ef þú slærð inn 6 viltausa stafi")
        with open('Nöfn.txt', 'r',encoding = 'utf-8') as f: # lesa textaskánna Nöfn.txt og setja í listann "orð"
            for line in f:
                orð = line.split(" ")
            #print(orð)
            while True:
                hengimann = Hengimann(orð)
                while not hengimann.buinn():
                    hengimann.prenta_orð_falið()
                    gisk = input("Giskaðu á staf: ")
                    hengimann.giska(gisk)
                    hengimann.prenta_gisk()
                    print()

                if hengimann.sigur():
                    staða[0] = staða[0] + 1# setja í lista ef þú vannst
                    print("Þetta er rétt hjá þér, nafnið er:",hengimann.svar)
                    print("-----------------ÞÚ VANNST--------------------")
                    Leikur_buinn = True
                else:
                    staða[1] = staða[1] + 1#setja í lista ef þú tapaðir
                    print("Rétt nafn er:",hengimann.svar)
                    print("-----------------ÞÚ TAPAÐIR-------------------")
                    Leikur_buinn = True

                if Leikur_buinn:
                    if Hengimann.spilaaftur():
                        Leikur_buinn = False
                    else:# ef þú hættir í leiknum þá prentast út hve oft þú vannst og tapaðir
                        print("Þú vannst",staða[0],"sinnum og tapaðir",staða[1],"sinnum.")
                        print()
                        break


    elif val == 2:
        print("Þú hefur valið að giska á dýr í Hangman")
        print("Þú tapar ef þú slærð inn 6 viltausa stafi")
        with open('Dýr.txt', 'r',encoding = 'utf-8') as f:# lesa textaskánna Dýr.txt og setja í listann "orð"
            for line in f:
                orð = line.split(" ")
            #print(orð)
            while True:
                hengimann = Hengimann(orð)
                while not hengimann.buinn():
                    hengimann.prenta_orð_falið()
                    gisk = input("Giskaðu á staf: ")
                    hengimann.giska(gisk)
                    hengimann.prenta_gisk()
                    print()
                if hengimann.sigur():
                    staða[0] = staða[0] + 1# setja í lista ef þú vannst
                    print("Þetta er rétt hjá þér, dýrið er:",hengimann.svar)
                    print("-----------------ÞÚ VANNST--------------------")
                    Leikur_buinn = True
                else:
                    staða[1] = staða[1] + 1#setja í lista ef þú tapaðir
                    print("Rétt nafn á dýri er:",hengimann.svar)
                    print("-----------------ÞÚ TAPAÐIR-------------------")
                    Leikur_buinn = True

                if Leikur_buinn:
                    if Hengimann.spilaaftur():
                        Leikur_buinn = False
                    else:
                        print("Þú vannst",staða[0],"sinnum og tapaðir",staða[1],"sinnum.")
                        print()
                        break



    elif val == 3:
        print("Þú hefur valið að giska á lönd í Hangman")
        print("Þú tapar ef þú slærð inn 6 viltausa stafi")
        with open('Lönd.txt', 'r',encoding = 'utf-8') as f:# lesa textaskánna Lönd.txt og setja í listann "orð"
            for line in f:
                orð = line.split(" ")
            #print(orð)
            while True:
                hengimann = Hengimann(orð)
                while not hengimann.buinn():
                    hengimann.prenta_orð_falið()
                    gisk = input("Giskaðu á staf: ")
                    hengimann.giska(gisk)
                    hengimann.prenta_gisk()
                    print()
                if hengimann.sigur():
                    staða[0] = staða[0] + 1# setja í lista ef þú vannst
                    print("Þetta er rétt hjá þér, landið er:",hengimann.svar)
                    print("-----------------ÞÚ VANNST--------------------")
                    Leikur_buinn = True
                else:
                    staða[1] = staða[1] + 1#setja í lista ef þú tapaðir
                    print("Rétt land er:",hengimann.svar)
                    print("-----------------ÞÚ TAPAÐIR-------------------")
                    Leikur_buinn = True

                if Leikur_buinn:
                    if Hengimann.spilaaftur():
                        Leikur_buinn = False
                    else:
                        print("Þú vannst",staða[0],"sinnum og tapaðir",staða[1],"sinnum.")
                        print()
                        break

    elif val == 4:#Liður 4 = hætta í forritinu

        print("Takk fyrir að keyra forritið")
        byrjun = 1
    else:
        print("Þú hefur valið vitlaust, reyndu aftur")
        print()





