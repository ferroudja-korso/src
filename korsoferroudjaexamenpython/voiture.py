

import Vehicles



class Voiture(Vehicles):
    type_vehicles = "Voiture"
    liste_energie = ["diesel", "essence", "hybride"]

    def __init__(self, immat, annee, modele, marque, nb_roues, prix, couleur, vitesse, kilometrage, nb_places, energie):
        super().__init__(immat, annee,modele, marque, nb_roues, prix, couleur, vitesse, kilometrage)
        self.nb_places = self.set_nb_places(nb_places)
        self.energie = self.set_energie(energie)

    def get_nb_places(self):
        return self.nb_places
    
    def get_energie(self):
        return self.energie
    
    def set_nb_places(self, nb_places):
        if nb_places >= 3 & nb_places <= 7:
            self.nb_places = nb_places
        else:
            print("Nombres de places hors normes!")

    def set_energie(self, energie):
        if energie in self.liste_energie:
            self.energie = energie
        else:
            print("Energie non reconnue !")
    



