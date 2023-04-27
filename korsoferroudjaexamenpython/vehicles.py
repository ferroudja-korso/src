class Vehicles:

    class_name = "Véhicule Générique"


    def __init__(self, immatriculation, annee, modele, marque, nb_roues, prix, couleur, vitesse_max, compteur) :
        self.immatriculation = immatriculation
        self.premiere_annee_circu = annee
        self.modele = modele 
        self.marque = marque
        self.nb_roues = nb_roues
        self.prix = prix
        self.couleur = couleur
        self.vitesse_max = vitesse_max
        self.compteur = compteur

    def get_immatriculation(self): 
        return self.immatriculation
    
    def get_annee(self):
        return self.premiere_annee_circu
    
    def get_modele(self):
        return self.modele
    
    def get_marque(self):
        return self.marque
    
    def get_nb_rous(self):
        return self.nb_roues
    
    def get_prix(self):
        return self.prix
    
    def get_couleur(self):
        return self.couleur
    
    def get_vitesse_max(self):
        return self.vitesse_max
    
    def get_compteur(self):
        return self.compteur
    
    def set_modele(self, modele):
        self.modele = modele

    def set_immatriculation(self, immat):
        self.immatriculation = immat

    def set_annee(self, annee):
        self.premiere_annee_circu = annee

    def set_marque(self, marque):
        self.marque = marque

    def set_nb_roues(self, nb_roues):
        self.nb_roues = nb_roues

    def set_prix(self, prix):
        self.prix = prix

    def set_vitesse_max(self, vitesse):
        self.vitesse_max = vitesse

    def set_compteur(self, kilometrage):
        self.compteur = kilometrage

    
    # Autre méthodes utiles

    def decrire_vehicles(self):
        print("Véhicule de type", self.class_name)
        print("Un véhicule générique ne peut être décrit !")