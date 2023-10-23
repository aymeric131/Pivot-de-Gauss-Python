
def pivot(A):
    nbLignes = len(A)
    nbCols = len(A[0])
    lastRow = A[nbLignes - 1]
    nbVar = nbCols - 1
    nbVarEcart = nbLignes - 1
    domaine = nbVar - nbVarEcart

    while (max(lastRow) > 0):
        q = (lastRow.index(max(lastRow)))  # indice de la colonne pivot
        print(("\nLa colonne pivot est la colonne n° : " + str(q + 1)))
        r = (10 ** 20)  # On attribue au ratio une grande très valeure pour l'initialiser

        for i in range(0, nbLignes - 1):
            # Calcul du ratio
            if (A[i][q] != 0):
                res = (A[i][nbCols - 1]) / (A[i][q])
                if ((res > 0) and (res <= r)):
                    r = res
                    x = i;  ## Récupération de l'indice du ratio minimum

        print("La ligne pivot est la ligne n° : " + str(x + 1), "\n")

        tab = [[0] * nbCols for i in range(nbLignes)]

        # Pivotement

        # Transformation de la ligne pivot
        for j in range(0, nbCols):
            tab[x][j] = (1 / (A[x][q])) * (A[x][j])
            tab[x][j] = round(tab[x][j], 3);

        # Transformation des autres lignes
        for i in range(0, nbLignes):
            if (i != x):
                for k in range(0, nbCols):
                    tab[i][k] = A[i][k] - ((A[i][q]) / (A[x][q]) * A[x][k])
                    tab[i][k] = round(tab[i][k], 3);

        A = tab;
        lastRow = A[nbLignes - 1]

        # Affichage du tableau
        print("Voici le nouveau tableau après pivotement :")

        for i in range(0, nbLignes):
            print(A[i]);

    print("\nLa fonction est maximisée !\n")
    maximum = abs(lastRow[-1])

    #Recherche des points
    P = []
    PointsInter = [0] * nbVar

    ind = 0
    for i in range(0, nbVar):
        base = 0
        c = 0
        a = 0
        for j in range(0, nbVarEcart):
            P.append(A[j][i])
        for k in range(0, len(P)):
            if P[k] == 1:
                c += 1
            elif P[k] != 0:
                a += 1
            else:
                base = 0

        if c == 1 and a == 0:
            base = 1
        if base == 1:
            ind = P.index(max(P))
            PointsInter[i] = A[ind][-1]
        else:
            PointsInter[i] = 0
        P = []

    # Affichage des points
    Points = [0] * domaine
    for l in range (0,domaine):
        Points[l] = PointsInter[l]

    print("Voici les points :", Points)

    #Affichage du maximum
    print("Le maximum est", maximum);
