#Lárus Óskar Lárusson
#FOR1TÖ05BD
#2017
#Lokaverkefni


import random

# TODO: lesa inn orð úr orðaskrá
# TODO: Dickt, list, föll, klasar
# TODO: reyna setja mynd HANGMAN


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

    orð = []
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






    if val == 1: # ef valið er 1 í valmynd
        print("Þú hefur valið Nöfn í Hangman")
        print("Þú tapar ef þú slærð inn 6 viltausa stafi")
        with open('Nöfn.txt', 'r',encoding = 'utf-8') as f: # lesa textaskánna Nöfn.txt og setja í listann "orð"
            for line in f:
                orð = line.split(" ")
            print(orð)
            while True:
                hengimann = Hengimann(orð)
                while not hengimann.buinn():
                    hengimann.prenta_orð_falið()
                    gisk = input("Giskaðu á staf: ")
                    hengimann.giska(gisk)
                    hengimann.prenta_gisk()
                    print()

                if hengimann.sigur():
                    print("Þetta er rétt hjá þér, nafnið er:",hengimann.svar)
                    print("-----------------ÞÚ VANNST--------------------")
                    break
                else:
                    print("Rétt nafn er:",hengimann.svar)
                    print("-----------------ÞÚ TAPAÐIR-------------------")
                    break








    elif val == 2:
        print("Þú hefur valið Dýr í Hangman")
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
                    print("Þetta er rétt hjá þér, dýrið er:",hengimann.svar)
                    print("-----------------ÞÚ VANNST--------------------")
                    break
                else:
                    print("Rétt nafn á dýri er:",hengimann.svar)
                    print("-----------------ÞÚ TAPAÐIR-------------------")
                    break








    elif val == 3:
        print("Þú hefur valið Lönd í Hangman")
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
                    print("Þetta er rétt hjá þér, landið er:",hengimann.svar)
                    print("-----------------ÞÚ VANNST--------------------")
                    break
                else:
                    print("Rétt land er:",hengimann.svar)
                    print("-----------------ÞÚ TAPAÐIR-------------------")
                    break









