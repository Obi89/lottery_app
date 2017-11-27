import random

def lotto_zahlen(nr):
    lot_liste = []
    while True:
        if len(lot_liste) == nr:
            break
        lot_nb = random.randint(1, 50)
        if lot_nb not in lot_liste:
            lot_liste.append(lot_nb)
    return lot_liste


def lot():
    lot_numbers = int(7)
    return lotto_zahlen(lot_numbers)


if __name__ == "__main__":
    lot()