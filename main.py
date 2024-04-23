import fltk
import fonctions_hex_color
import import_txt
import os
tableau=import_txt.data_tab("fichiers fournis/fichiers fournis/maps-texte/map1.txt")
#os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"

couleur=fonctions_hex_color.couleur
scaler=15
longueur=tableau[1]
hauteur=tableau[2]
print(longueur,hauteur)


class Jeu:
    def __init__(self,coo=(0,0),scaler=scaler,longueur=longueur,hauteur=hauteur):
        self.state_open=False
        self.coo=coo
        self.tableau_affiché=False
    def coo_scaler(self,coo_input,scaler):
        """
        coo_input : tuple (int,int)
        scaler : int (self.scaler en général mais pas toujours)
        prend en paramètre des coordonnées telles qu'interprétées dans le schéma de données
        ex : (1,1)
        et renvoit les coordonnées en pixel du point du tableau
        par rapport à l'offset par rapport à l'origine que représente self.coo
        """
        return (self.coo[0]+(coo_input[0]*scaler),self.coo[1]+(coo_input[1]*scaler))
    
    def coordonnées(self,coo):
        """
        transforme des coordonnées pixel en coordonnées de tableau
        """
        return((coo[0]-self.coo[0])//self.scaler,(coo[1]-self.coo[1])//self.scaler)
    
    def carré(self,coo,luminance=1,contour="white"):
        """
        coo : tuple (int,int)
        crée un carré aux coordonnées données
        les coordonnées sont des coordonnées tableau 
        ex : (2,1)
        """

        coo_plus_1=(coo[0]+1,coo[1]+1)
        if luminance=="#":
            couleur_rectangle=fonctions_hex_color.random_green()
            couleur_contour=couleur_rectangle
        elif luminance==".":
            couleur_rectangle=fonctions_hex_color.random_hex(145,155)
            couleur_contour=couleur_rectangle
        elif luminance==">":
            couleur_rectangle=fonctions_hex_color.random_hex(200,255)
            couleur_contour=couleur_rectangle
        elif luminance=="*":
            couleur_rectangle=fonctions_hex_color.random_hex(175,185)
            couleur_contour=couleur_rectangle
        fltk.rectangle(self.coo_scaler(coo,self.scaler)[0],self.coo_scaler(coo,self.scaler)[1],self.coo_scaler(coo_plus_1,self.scaler)[0],self.coo_scaler(coo_plus_1,self.scaler)[1],couleur=couleur_contour,remplissage=couleur_rectangle,tag="cases")

    def texte(self,coo,texte,police="Tekton Pro",couleur="black"):
        coo_pixel=self.coo_scaler(coo,self.scaler)
        fltk.texte(coo_pixel[0],coo_pixel[1],texte,couleur,"nw",police,15,"indices")
    def cree_fenetre(self):
        fltk.cree_fenetre(self.size_x,self.size_y,60)
    
    def run(self):
        if not self.state_open:
            self.state_open=True
            self.cree_fenetre()
        else:
            fltk.ferme_fenetre()
            self.cree_fenetre()
    

    def lecture_tableau(self,tab:list):
        for i in range(len(tab)):
            for j in range(len(tab[i])):
                self.carré((j,i),tab[i][j])

    def lecture_indices(self,tab:list):
        for loop in range(len(tab[0])):
            self.texte((loop,-1),tab[0][loop])
        for loop in range(len(tab[1])):
            self.texte((-1,loop),tab[1][loop])


    def efface_tableau(self):
        fltk.efface("cases")

    
    def actualise_tableau(self,tab):
        if self.tableau_affiché:
            self.efface_tableau()
            self.lecture_tableau(tab)
        else:
            self.tableau_affiché=True
            self.lecture_tableau(tab)
    #---------------------------------------------------scenes--------------------------------------
    def menu(self):
        self.size_x=1200
        self.size_y=800
        self.run()
        if self.state_open:
            fltk.rectangle(0,0,self.size_x,self.size_y,remplissage=fonctions_hex_color.hex_converter(couleur),couleur="white")

    def jeu_start(self,map):
        maps=os.listdir("fichiers fournis/fichiers fournis/maps-texte")
        tableau=import_txt.data_tab("fichiers fournis/fichiers fournis/maps-texte/map1.txt")
        couleur=fonctions_hex_color.couleur
        scaler=15
        longueur=tableau[1]
        self.hauteur=tableau[2]
        self.size_x=self.coo[0]+(longueur*scaler)
        self.size_y=self.coo[1]+(hauteur*scaler)
        self.state_open=False
        self.scaler=scaler
        self.tableau_affiché=False



condition=True



jeu=Jeu()
jeu.run()
jeu.menu()


while condition:
    fltk.mise_a_jour()
    eve=fltk.donne_ev()
    typeeve=fltk.type_ev(eve)
    if typeeve=='Quitte':
        condition = False
fltk.ferme_fenetre()