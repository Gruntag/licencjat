import secrets


def rabin_miller(p, ilosc_prob=25):
    d = p - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d = d // 2
    for _ in range(ilosc_prob):
        a = secrets.randbelow(p - 3) + 2
        x = pow(a, d, p)
        if x != 1 and x != p - 1:
            j = 1
            while j < s and x != p - 1:
                x = pow(x, 2, p)
                if x == 1:
                    return False
                j += 1
            if x != p - 1:
                return False
    return True


def generuj_pierwsze(dlugosc, ilosc_prob=25):  # dlugosc czyli oczekiwana dlugosc liczby wyniokwej
    if dlugosc // 2 - 4 <= 0:
        raise ValueError("Too small dlugosc. Dlugosc must be greater than 12.")
    return [generuj_pierwsza(dlugosc // 2 - 1, ilosc_prob), generuj_pierwsza(dlugosc // 2 + 1, ilosc_prob)]


def generuj_pierwsza(dlugosc, ilosc_prob=25):
    if dlugosc < 1:
        raise ValueError("too small limit.")
    liczba = secrets.randbits(dlugosc)
    while not rabin_miller(liczba, ilosc_prob):
        liczba = secrets.randbits(dlugosc)
    return liczba
