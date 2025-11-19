from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass


class Car(Vehicle):

    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model

    def start_engine(self) -> None:
        print(f"{self.make} {self.model}: Двигун запущено")


class Motorcycle(Vehicle):

    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model

    def start_engine(self) -> None:
        print(f"{self.make} {self.model}: Мотор заведено")


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str):
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str):
        pass


class USVehicleFactory(VehicleFactory):
    region = "US Spec"

    def create_car(self, make: str, model: str) -> Car:
        return Car(make, f"{model} ({self.region})")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, f"{model} ({self.region})")


class EUVehicleFactory(VehicleFactory):
    region = "EU Spec"

    def create_car(self, make: str, model: str) -> Car:
        return Car(make, f"{model} ({self.region})")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, f"{model} ({self.region})")


def main():
    us_factory = USVehicleFactory()
    vehicle1 = us_factory.create_car("Toyota", "Corolla")
    vehicle1.start_engine()

    eu_factory = EUVehicleFactory()
    vehicle2 = eu_factory.create_motorcycle("Harley-Davidson", "Sportster")
    vehicle2.start_engine()


if __name__ == "__main__":
    main()
