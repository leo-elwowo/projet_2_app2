def data_tab(fichier):
    file = open(fichier, "r")
    lignes = file.read()
    lignes=lignes.splitlines()
    hauteur=len(lignes)
    longueur=len(lignes[0])
    resultats=[]
    for loop in lignes:
        temp=[]
        for i in loop:
            temp.append(i)
        resultats.append(temp)
    file.close()
    return (resultats,longueur,hauteur)