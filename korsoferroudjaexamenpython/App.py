
import Vehicles
import Voiture
import Camion
import Moto


class App:
    application_name = "Gestion of vehicles"
    liste_vehicles =[]

    def __init__(self, liste_vehicles) -> None:
        self.liste_vehicles=liste_vehicles
        
    def get_vehicles(self):
        return self.liste_vehicles
    
    def set_vehicles(self, liste_veh):
        self.liste_vehicles = liste_veh

    def get_statistique(self):
        if len(self.liste_vehicles) == 0:
            print("Liste de véhicules vide !\n Aucune statistique à afficher")
        else:
            for vehicles in self.liste_vehicles:
                Vehicles.vehicles.decrire_vehicles()

if __name__ == "__main__":
    application = App([])

    application.get_statistique()
vehi = Vehicles(100, 2020, "Man", 350, 10, 1500, "red", 20250, 120)
vehi.decrire()
    