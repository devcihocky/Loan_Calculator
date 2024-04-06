# Rozmiar kwadratu
n = 6

# Pętla przez wiersze
for i in range(n):
    # Pętla przez kolumny
    for j in range(n):
        # Sprawdzenie, czy jesteśmy na krawędzi kwadratu
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("* ", end="")
        else:
            print("  ", end="")
    # Przejście do nowej linii po każdym wierszu
    print()
