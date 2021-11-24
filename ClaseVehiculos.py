from dataclasses import dataclass

@dataclass
class ClaseVehiculos:
    marca: str
    modelo: str

    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        