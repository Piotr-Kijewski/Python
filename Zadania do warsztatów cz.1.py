# Dane do zadań

lista_imion = ["Filip", "Damian", "Jan", "Jadwiga", "Zygmunt"]
liczba_1 = 2
liczba_2 = 10

# 1. Wypisz drugie imię z listy 'lista_imion'
print('1. Wypisz drugie imię z listy lista_imion:')
print(lista_imion)

print(lista_imion[1])

# 2. Zmień imię Zygmunt na Ilona
print('2.Zmien imie Zygmunt na Ilona')
print(lista_imion)

lista_imion[4] = 'Ilona'
print(lista_imion)

# 3. Dodaj nowe imię 'Pawel' do listy (na koniec listy)
print('3. Dodaj nowe imie Pawel do listy (na koniec listy)')
print(lista_imion)

lista_imion.append('Pawel')
print(lista_imion)

# 4. Dodaj nowe imię do list 'Agata' jako drugie
print('4. Dodaj nowe imie do list Agata jako drugie')
print(lista_imion)

lista_imion.insert(1, 'Agata')
print(lista_imion)

# 5. Usuń z listy imię Jadwiga
print('5. Usuń z listy imię Jadwiga')
print(lista_imion)

del lista_imion[4]
print(lista_imion)

# lub 

lista_imion.insert(4, 'Jadwiga') # dodanie rekordu do tablicy
print(lista_imion)

lista_imion.remove("Jadwiga")
print(lista_imion)

# 6. Wypisz ilość imion w liście (uzywając do tego odpowiedniej metody)
print('6. Wypisz ilosc imion w liscie uzywajac do tego odpowiedniej metody')
print(lista_imion)

print(len(lista_imion))

# 7. Pomnóz dwie zmienne: liczba_1 oraz liczba_2 i wypisz
print('7. Pomnoz dwie zmienne: liczba_1 oraz liczba_2 i wypisz')
print('Liczba_1 =', liczba_1)
print('Liczba_2 =', liczba_2)
print('Wynik:')

print(liczba_1 * liczba_2)

# 8. Sprawdź uzywając warunków if/else która zmienna: liczba_1 oraz liczba_2 jest większa i wypisz odpowiedni tekst na ekranie
print('8. Która zmienna, liczba_1 czy liczba_2 jest większa i wypisz odpowiedni tekst')
print('Liczba_1 =', liczba_1)
print('Liczba_2 =', liczba_2)
print('Wynik:')

if liczba_1 > liczba_2:
    print('Liczba_1 jest większa od liczba_2.')
else:
    print('Liczba_1 jest mniejsza od liczba_2.')

# 9. Sprawdź czy na liście imion znajduje się imię 'Jan' i wypisz odpowiedni komunikat
print('9. Sprawdz czy na liscie imion znajduje sie imie Jan i wypisz odpowiedni komunikat')
print(lista_imion)

if "Jan" in lista_imion:
  print("Na liście jest imie Jan")
else:
  print("Na liscie nie ma imienia Jan")

# 10. Sprawdź czy na liście imion znajduje się imię 'Jan', jezeli tak to sprawdź czy liczba_2 jest większa od liczba_1, jezeli tak to wypisz na ekran drugie i trzecie imię z listy imion
print('10. Warunki: Sprawdz czy na liscie imion znajduje się imie Jan, jezeli tak to sprawdz czy liczba_2 jest wieksza od liczba_1, jezeli tak to wypisz na ekran drugie i trzecie imie z listy imion')
print(lista_imion)
print('Liczba_1 =', liczba_1)
print('Liczba_2 =', liczba_2)

if "Jan" in lista_imion:
  if liczba_2 > liczba_1:
    print(lista_imion[1:3])
  
# 11. Zmień typ liczba_1 na string a następnie wypisz na ekran
print('11. Zmien typ liczba_1 na string a następnie wypisz na ekran')

tekst = str(liczba_1)
print(tekst)

# lub

print(str(liczba_1))

# 12. Zmień typ liczba_2 na float i dodaj do niej liczbę 24.5 i wypisz na ekran
print('12. Zmien typ liczba_2 na float i dodaj do niej liczbe 24.5 i wypisz na ekran')
print('Liczba_2 =', liczba_2)

print(float(liczba_2) + 24.5)

# 13. Wypisz tekst na ekran: 'Wartość liczby_2 to: [tutaj ma się pojawić wartość ze zmiennej]'
print('13. Wypisz tekst na ekran: Wartosc liczby_2 to: [tutaj ma sie pojawic wartosc ze zmienjnej]')

print('Wartosc liczby_2 to: ' + str(liczba_2))
# lub
print('Wartosc liczby_2 to:', liczba_2)
# lub
print(f'Wartosc liczby_2 to: {liczba_2}')

# 14. Sprawdź czy liczba_2 jest większa od liczba_1 LUB lista imion zawiera imię 'Zygmunt' i wypisz na ekranie odpowiedni komunikat.
print('14. Sprawdz czy liczba_2 jest wieksza od liczba_1 LUB lista imion zawiera imie Zygmunt i wypisz na ekranie odpowiedni komunikat')

if liczba_2 > liczba_1 or 'Zygmunt' in lista_imion:
    print('Liczba_2 jest wieksza od liczba_1 lub lista imion zawiera imie: Zygmunt')
else:
    print('Liczba_2 nie jest wieksza od liczba_1 a lista imion nie zawiera imie: Zygmunt')

# 15. * Stwórz nową listę która zawiera 5 elementów losowo wybranych cyfr a następnie dodaj wszystkie elementy do siebie i wypisz na ekranie 
# (tak aby mozna było dynamicznie rozszerzeć wielkość tablicy i zeby suma się liczyła za kazdym razem poprawnie)
print('15. Stworz nowa lista ktora zawiera 5 elementow losowo wybranych cyfr a nastepnie dodaj wszystkie elementy do siebie i wypisz na ekranie')

nowa_lista = [10, 3, 73, 52, 8]
print(nowa_lista)
print(sum(nowa_lista))
# lub
print(sum(nowa_lista[:]))

nowa_lista.append(53)
print(nowa_lista)
print('Suma tablicy:', sum(nowa_lista))

# 16. * Przeiteruj po wszystkich elementach stworzonej listy w pkt 15 i wypisz je na ekran podnosząc kazdą wartość do potęgi 2
print('16. Przeiteruj po wszystkich elementach stworzonej listy w pkt 15 i wypisz je na ekran podnoszac kazda wartosc do potegi 2')

i=0
for i in nowa_lista:
    potega = i**2
    print('Podniesienie elementu do potegi z listy i wypisanie go:', i, '^2')
    print(potega)