import model

potovanje = model.Potovanje(stanje1=0, stanje2=0)

def placilo1():
    placal1 = float(input('Znesek, ki ga je plačala prvi potnik: '))
    potovanje.stanje1 += placal1
    print('Prvi do sedaj plačal {0}, drugi pa {1}.'.format(potovanje.stanje1, potovanje.stanje2))
    return potovanje.nasvet()

def placilo2():
    placal2 = int(input('Znesek, ki ga je plačala prvi potnik: '))
    potovanje.stanje2 += placal2
    print('Prvi do sedaj plačal {0}, drugi pa {1}.'.format(potovanje.stanje1, potovanje.stanje2))
    return potovanje.nasvet()
    

def konec_potovanja():
    return potovanje.konec_potovanja()
  

def stroski_na_osebo():
    return potovanje.stroski_na_osebo()

def pozdrav():
    print('Živjo, ta program vama bo pomagal spremnljati stroške potovanja. Določita, kdo bo prvi in kdo drugi potnik. Srečno pot!') 

def kaj_zelita():
    print('Kaj želita?')
    print('1) Zabeležiti strošek prvega potnika.')
    print('2) Zabeležiti strošek drugega potnika.')
    print('3) Končati potovanje.')
    print('4) Izvedeti, koliko sta do sedaj zapravila na osebo.')
    izbira = input('> ')
    return naslednji_korak(izbira)

def naslednji_korak(izbira):
    if izbira == '1':
        placilo1()
    elif izbira == '2':
        placilo2()
    elif izbira == '3':
        konec_potovanja()
    elif izbira == '4':
        stroski_na_osebo()
    else:
        return print('Izbrati morata eno od zgornjih možnosti.')

def stroski_potovanja():
    pozdrav()
    while True:
        kaj_zelita()
        continue



stroski_potovanja()