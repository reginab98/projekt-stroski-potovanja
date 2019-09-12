#To je kalkulator stroškov na potovanju za dve osebi.

class Potovanje:

    def __init__(self, stanje1, stanje2):
        self.stanje1 = 0
        self.stanje2 = 0

    def placilo1(self, placal1):
        self.stanje1 += placal1

    def placilo2(self, placal2):
        self.stanje2 += placal2

    def nasvet(self):
        if self.stanje1 > self.stanje2:
            print('Naslednjič naj plača prvi potnik')
        elif  self.stanje2 > self.stanje1:
            print('Naslednjič naj plača drugi potnik')
        else:
            print('Vseeno je, kdo nasledjič plača.')

    def stroski_na_osebo(self):
        stroski_na_osebo = (self.stanje1 + self.stanje2) / 2
        print ('Do sedaj sta zapravila {0} EUR na osebo'.format(stroski_na_osebo))
    
    def konec_potovanja(self): #Ko se potovanje konča, se izpiše, kdo naj komu koliko vrne.
        if self.stanje1 > self.stanje2:
            print('Drugi potnik mora prvemu plačati {} evrov.'.format((self.stanje1 - self.stanje2) / 2 ))
        elif self.stanje2 > self.stanje1:
            print('Prvi potnik mora drugemu plačati {} evrov.'.format((self.stanje2 - self.stanje1) / 2 ))
        else:
            print('Nihče ni nikomur nič dolžan.')

    




         


    

