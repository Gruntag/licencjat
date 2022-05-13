import math
import pierwsze
import secrets
import kodolamacze
import Do_Not_Touch

OBSLUGIWANE = 18446744073709551616  # 2^64 obslugiwana dlugosc wejscia


def zapisz_plik(dane, nazwa):
    f = open(nazwa, "wb")
    f.write(dane)


def czytaj_plik(nazwa):
    with open(nazwa, "rb") as f:
        return f.read()


def generuj_klucze(p, q):
    l = math.lcm(p - 1, q - 1)
    e = secrets.randbelow(l - 2) + 2
    while not math.gcd(e, l) == 1:
        e = secrets.randbelow(l - 2) + 2
    private_key = [p * q, pow(e, -1, l)]
    public_key = [p * q, e]
    zapisz_plik(private_key, "private key.txt")
    zapisz_plik(public_key, "public key.txt")


def szyfruj(dane, klucz):
    return pow(dane, klucz[1], klucz[0])


def odszyfruj(dane, klucz):
    return pow(dane, klucz[1], klucz[0])


def serializuj(dane):
    wynik = 0
    mnoznik = 1
    for numer in range(len(dane)):
        wynik += dane[numer] * mnoznik
        mnoznik *= 256
    wynik_ostateczny = wynik * OBSLUGIWANE + len(dane)
    return wynik_ostateczny


def deserjalizuj(dane):
    wynik = []
    dlugoscdanych = dane % OBSLUGIWANE
    d = dane // OBSLUGIWANE
    for numer in range(dlugoscdanych):
        wynik.append(d % 256)
        d = d // 256
    return bytes(wynik)


# def dlugosc_danych(dlugosc):
#     wynik = []
#     d = dlugosc
#     for numer in range(8):
#         wynik.append(d % 256)
#         d = d // 256
#     return wynik


# dane = czytaj_plik("dane.txt")
# seria = serializuj(dane)
# powrot = deserjalizuj(seria)
# zapisz_plik(powrot, "wynik.txt")


# def sito(n):
#     wielka_tablica_prawdy = []
#     for x in range(2, int(n)):
#         jest_pierwsza = True
#         for pierwsza in wielka_tablica_prawdy:
#             if x % pierwsza == 0:
#                 jest_pierwsza = False
#                 break
#         if jest_pierwsza:
#             wielka_tablica_prawdy.append(x)
#     print(wielka_tablica_prawdy)

#for p in Do_Not_Touch.WIELKA_TABLICA_PIERWSZOSCI[2:]:
#    print(Pierwsze.rabin_miller(p, n)," " , p)


print(pierwsze.generuj_pierwsze(10))

# print(x[0] * x[1])
# print(kodolamacze.faktoryzacja_algorytmem_fermata(x[0] * x[1]))
# print(kodolamacze.faktoryzacja_algorytmem_brute_force(990469 * 89819))
# print(kodolamacze.faktoryzacja_algorytmem_pollarda(x[0] * x[1]))
#







