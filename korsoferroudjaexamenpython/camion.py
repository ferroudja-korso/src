
import Vehicles

class Camion(Vehicles):
    type_vehicles = "Camion"

    def __init__(self, immat, annee, modele, marque, nb_roues, prix, couleur, vitesse, kilometrage, charge):
        super().__init__(immat, annee,modele, marque, nb_roues, prix, couleur, vitesse, kilometrage)
        self.charge_utile = self.set_charge(charge)

    def get_charge(self):
        return self.charge_utile
    
    def set_charge(self, charge):
        if charge > 0:
            self.charge_utile = charge
        else:
            print("La charge ne peut être négative!")
        




