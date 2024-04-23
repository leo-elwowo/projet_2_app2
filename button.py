import fltk
class Button:
    def __init__(self,coo,scaler,offset,text,img=None,tag="bouton",color="white",taille_x=4,taille_y=1):
        self.coo=coo
        self.scaler=scaler
        self.offset=offset
        self.taille_x=taille_x
        self.taille_y=taille_y


        self.coo_plus_1=(self.coo[0]+self.taille_x,self.coo[1]+self.taille_y)
        self.pixel_coo=(self.offset[0]+(self.coo[0]*self.scaler),self.offset[1]+(self.coo[1]*self.scaler))
        self.pixel_coo_plus_1=(self.offset[0]+((self.coo[0]+self.taille_x)*self.scaler),self.offset[1]+(self.coo[1]+self.taille_y)*self.scaler)
        self.milieu=(self.pixel_coo[0]+((self.pixel_coo_plus_1[0]-self.pixel_coo[0])//2),self.pixel_coo[1]+((self.pixel_coo_plus_1[1]-self.pixel_coo[1])//2))

        self.color=color
        self.text=text[:18] #pour que le texte ne dépasse pas la case
        self.tag=tag
        self.img=img
        self.state=True
        self.index=self.coo[1]

    def coo_scaler(self,coo_input,scaler):
        """
        renvoit les coordonnées en pixels d'un point en coordonnées tableau.
        ex : 
        >>> self.coo_scaler((3,4),50)
        >>> (950, 200)
        les résultats au dessus ne sont pas exhaustifs
        """
        return (self.offset[0]+(coo_input[0]*scaler),self.offset[1]+(coo_input[1]*scaler))

    def draw(self):
        
        couleur_rectangle=self.color
        if self.img==None:
            fltk.rectangle(self.coo_scaler(self.coo,self.scaler)[0],self.coo_scaler(self.coo,self.scaler)[1],self.coo_scaler(self.coo_plus_1,self.scaler)[0],self.coo_scaler(self.coo_plus_1,self.scaler)[1],couleur=couleur_rectangle,remplissage=couleur_rectangle,tag=self.tag)
        else:
            fltk.image(x=self.milieu[0],y=self.milieu[1],largeur=self.scaler*self.taille_x,hauteur=self.scaler*self.taille_y,fichier=self.img,ancrage="center",tag=self.tag)
        fltk.texte(self.milieu[0],self.milieu[1],self.text,"black","center","MS Gothic",16,tag=self.tag)

    def state_set(self):
        self.state=not self.state
        return self.state
    
    def clicked(self,eve):
        if fltk.type_ev(eve)=='ClicGauche':

            if self.state:
                return (self.pixel_coo[0]<fltk.abscisse_souris()<self.pixel_coo_plus_1[0])and(self.pixel_coo[1]<fltk.ordonnee_souris()<self.pixel_coo_plus_1[1])
            else:
                return False