def pgcd(a, b):
    """Calcul du PGCD de 2 entiers a et b.
    
    Parameters
    ----------
    a : int
        Premier entier.
    b : int
        Deuxième entier.

    Returns
    -------
    int
        Le PGCD de a et b.
    """
    while b != 0:
        a, b = b, a % b
    return a
