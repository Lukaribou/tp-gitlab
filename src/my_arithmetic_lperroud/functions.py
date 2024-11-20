def pgcd(a, b):
    """Calcul du PGCD de 2 entiers a et b."""
    while b != 0:
        a, b = b, a % b
    return a
