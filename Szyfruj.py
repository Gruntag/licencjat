import math
from typing import List
import pierwsze
import secrets
import kodolamacze
import Do_Not_Touch

OBSLUGIWANE = 18446744073709551616  # 2^64 obslugiwana dlugosc wejscia


def zapisz_plik(dane: bytes, nazwa: str):
    with open(nazwa, "wb") as f:
        f.write(dane)


def czytaj_plik(nazwa: str) -> bytes:
    with open(nazwa, "rb") as f:
        return f.read()


def generuj_klucze(p, q):
    l = (p - 1) * (q - 1) // math.gcd(p - 1, q - 1)
    e = secrets.randbelow(l - 2) + 2
    while not math.gcd(e, l) == 1:
        e = secrets.randbelow(l - 2) + 2
    private_key = [p * q, pow(e, -1, l)]
    public_key = [p * q, e]
    return [private_key, public_key]


def zapisz_klucz(klucz: List[int], nazwa: str):
    with open(nazwa, "w") as f:
        f.write(str(klucz[0]))
        f.write("\n")
        f.write(str(klucz[1]))
        f.write("\n")


def czytaj_klucz(nazwa: str) -> List[int]:
    wynik = []
    with open(nazwa, "r") as f:
        wynik.append(int(f.readline()))
        wynik.append(int(f.readline()))
    return wynik

#
# zapisz_klucz([1234, 5678], "test.txt")
# print(czytaj_klucz("test.txt"))


def szyfruj(dane: int, klucz: List[int]) -> int:
    if dane >= klucz[0]:
        raise ValueError("data too large.")
    return pow(dane, klucz[1], klucz[0])




def odszyfruj(dane: int, klucz: List[int]) -> int:
    if dane >= klucz[0]:
        raise ValueError(f"data too large {dane.bit_length()} > {klucz[0].bit_length()}")
    return pow(dane, klucz[1], klucz[0])


def serializuj(dane: bytes) -> int:
    wynik = 0
    mnoznik = 1
    for numer in range(len(dane)):
        wynik += dane[numer] * mnoznik
        mnoznik *= 256
    wynik_ostateczny = wynik * OBSLUGIWANE + len(dane)
    return wynik_ostateczny


def deserializuj(dane: int) -> bytes:
    wynik = []
    dlugoscdanych = dane % OBSLUGIWANE
    d = dane // OBSLUGIWANE
    for numer in range(dlugoscdanych):
        wynik.append(d % 256)
        d = d // 256
    return bytes(wynik)

#
# z = serializuj(czytaj_plik("danep.txt"), czytaj_klucz("priv.txt"))
# w = deserializuj(z, czytaj_klucz("pub.txt"))
#
#
# for i in range(10000):
#     print(i)
#     z = bytes(b'894e'*i) * 15482
#     assert bytes(i) == deserializuj(serializuj(bytes(i), []), [])
#











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

# for p in Do_Not_Touch.WIELKA_TABLICA_PIERWSZOSCI[2:]:
#    print(Pierwsze.rabin_miller(p, n)," " , p)


# print(pierwsze.generuj_pierwsze(20))

# print(x[0] * x[1])
# print(kodolamacze.faktoryzacja_algorytmem_fermata(x[0] * x[1]))
# print(kodolamacze.faktoryzacja_algorytmem_brute_force(990469 * 89819))
# print(kodolamacze.faktoryzacja_algorytmem_pollarda(x[0] * x[1]))
#

# print(generuj_klucze(5, 7))
