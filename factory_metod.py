from abc import ABC, abstractmethod
import unittest


class Delivery(ABC):
    @abstractmethod
    def deliver(self):
        pass

class TruckDelivery(Delivery):
    def deliver(self):
        return "Deliver by land in a box"

class ShipDelivery(Delivery):
    def deliver(self):
        return 'Deliver by sea in a container'

class DeliveryFactory(ABC):
    @abstractmethod
    def create_delivery(self):
        pass

class LandDeliveryFactory(DeliveryFactory):
    def create_delivery(self):
        return TruckDelivery()

class SeaDeliveryFactory(DeliveryFactory):
    def create_delivery(self):
        return ShipDelivery()

land_factory = LandDeliveryFactory()
sea_factory = SeaDeliveryFactory()

land_delivery = land_factory.create_delivery()
sea_delivery = sea_factory.create_delivery()

print(land_delivery.deliver())  # Вывод: Deliver by land in a box
print(sea_delivery.deliver())   # Вывод: Deliver by sea in a container



