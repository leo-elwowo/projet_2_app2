import random

def random_hex(mini=150,maxi=255):
    """
    renvoit une couleur sous format hexadecimal
    la couleur est aléatoire, mais ne peut pas avoir de composante (en décimal) en dessous de min (defaut = 150) et au dessus de max
    """
    tab=[]
    for i in range(3):
        tab.append(random.randint(max(mini,0),min(maxi,255)))
    return hex_converter(tab)

def random_green():
    tab=[25,random.randint(230,255),50]
    return hex_converter(tab)


def hex_converter(tab):
    """
    tab : list [int,int,int]
    transforme une liste de int entre 0 et 255 en couleur héxadécimale
    """
    rendu=[]
    for loop in tab:
        rendu.append(loop)
    for loop in range(len(rendu)):
        if len(hex(rendu[loop])[2:])==1:
            adder="0"+hex(rendu[loop])[2:]
        else:
            adder=hex(rendu[loop])[2:]
        rendu[loop]=adder
    str_rendu="#"
    for loop in rendu:
        str_rendu+=loop
    return str_rendu

couleur=[180,210,220]
couleur_sombre=[i-50 for i in couleur]