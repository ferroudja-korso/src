
import Vehicles

class Moto(Vehicles):

    type_vehicles = "Moto"

    def __init__(self, immat, annee, modele, marque, nb_roues, prix, couleur, vitesse, kilometrage):
        super().__init__(immat, annee,modele, marque, nb_roues, prix, couleur, vitesse, kilometrage)


    def decrire_vehicles(self):
        print("je suis de type  ",self.type_vehicles))
        





