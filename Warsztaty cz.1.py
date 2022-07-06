# Warsztaty cz.1 - tak robimy komentarze
#print('Hello world')
#print(123)
#print(2j)
#print('piotrek')

zmienna_typu_int = 1

#print(zmienna_typu_int)
#print(zmienna_typu_int + 2)
#print(zmienna_typu_int, 2, 23)
#print(zmienna_typu_int, 2, 'Test')

zmienna_typu_string = 'Filip'

#print(zmienna_typu_string)
#print(zmienna_typu_string, 'Test')
#print('Nasza ' + 'zmienna ma wartosc: ' + zmienna_typu_string)
#print(f'Nasza zmienna ma wartosc: {zmienna_typu_string} + {zmienna_typu_int}')

zmienna_typu_float = 20.5
zmienna_typu_float2 = 5e10

#print(zmienna_typu_float)
#print(zmienna_typu_float + 2)
#print(zmienna_typu_float + 2.5)
#print(zmienna_typu_float2)

zmienna_typu_complex = 2j
#print(zmienna_typu_complex)

zmienna_3 = 1
#print(zmienna_3)

zmienna_3 = 'Test'
#print(zmienna_3)

zmienna_3 = 1
#print(zmienna_3)

tekst = str(zmienna_3)
#print('Test ' + tekst)

zmienno_przecinkowa = float(zmienna_3)
#print(zmienno_przecinkowa)

zmienna_typu_bool = True
#print(zmienna_typu_bool)

zmienna_typu_lista = [1, 34, 50, 'test', False, 2, zmienna_typu_bool]
#print(zmienna_typu_lista)

zmienna_typu_lista = [1, 34, 50, 2]
#print(zmienna_typu_lista)

zmienna_typu_lista_1 = ['Filip', 'Damian', 'Jan']
#print(zmienna_typu_lista_1)

#print(len(zmienna_typu_lista))
#print(zmienna_typu_lista[0])
#print(zmienna_typu_lista[-2])
#print(zmienna_typu_lista[:3])

zmienna_typu_lista.append(6)
#print(zmienna_typu_lista)

zmienna_typu_lista.insert(0, 500)
#print(zmienna_typu_lista)

zmienna_typu_lista.remove(50)
#print(zmienna_typu_lista)

del zmienna_typu_lista[0]
#print(zmienna_typu_lista)

zmienna_typu_lista[0] = 112
#print(zmienna_typu_lista)

zmienna_liczba = 111
#print(zmienna_liczba == 10)

#if zmienna_liczba ==10:
#    print('Weszliśmy do ifa')
#    print('Weszliśmy do ifa2')
#   if True:
#        print('Weszliśmy do ifa3')
#        if False:
#            print('Weszliśmy do ifa4')
#            print('Weszliśmy do ifa5')

if zmienna_liczba < 10:
    print('Liczba jest mniejsza od 10')
elif zmienna_liczba == 10:
    print('Liczba jest równa 10')
else:
    print('Liczba jest większa od 10')





















