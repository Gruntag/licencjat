import math
import Do_Not_Touch

def faktoryzacja_algorytmem_fermata(klucz):
    pierwiastek = math.sqrt(klucz)
    if pierwiastek == int(pierwiastek):
        return pierwiastek
    b = 1
    while True:
        kwadrat = klucz + b ** 2
        #print(kwadrat)
        if math.sqrt(kwadrat) == int(math.sqrt(kwadrat)):
            break
        b += 1
    return [int(math.sqrt(kwadrat) - b), int(math.sqrt(kwadrat) + b)]


def faktoryzacja_algorytmem_brute_force(klucz):
    for x in Do_Not_Touch.WIELKA_TABLICA_PIERWSZOSCI: # zamiast wielkiej tablicy mozna uzyc sita eratostenesa, wtedy zawsze sie uda, pytanie jedyne o czas
        if klucz/x % 1 == 0:
            return [int(klucz/x), x]
    return 0


def faktoryzacja_algorytmem_pollarda(klucz):
    wynik = 1
    n = 1
    while wynik == 1:
        wynik = math.gcd(klucz, pow(2, n) - 1)
        n += 1
    if wynik == klucz:
        return -1
    else:
        return [wynik, int(klucz/wynik)]













