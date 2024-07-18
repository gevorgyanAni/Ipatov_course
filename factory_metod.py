
class Button:
    def render(self):
        pass

class WindowsButton(Button):
    def render(self):
        return "Render a button in a Windows style."

class HTMLButton(Button):
    def render(self):
        return "Render a button in HTML style."

class Dialog:
    def create_button(self):
        pass

    def render(self):
        button = self.create_button()
        return button.render()

class WindowsDialog(Dialog):
    def create_button(self):
        return WindowsButton()

class WebDialog(Dialog):
    def create_button(self):
        return HTMLButton()

# Использование
dialog = WindowsDialog()
print(dialog.render())  # Вывод: Render a button in a Windows style.

dialog = WebDialog()
print(dialog.render())  # Вывод: Render a button in HTML style.


import abc
class Delivery():
    def deliver(self):
        pass

class TruckDelivery(Delivery):
    pass

class ShipDelivery(Delivery):
    pass

class DeliveryFactory():
    pass

class LandDeliveryFactory(DeliveryFactory):
    pass

class SeaDeliveryFactory(DeliveryFactory):
    pass

land_factory = LandDeliveryFactory()
sea_factory = SeaDeliveryFactory()

land_delivery = land_factory.create_delivery()
sea_delivery = sea_factory.create_delivery()

print(land_delivery.deliver())  # Вывод: Deliver by land in a box
print(sea_delivery.deliver())   # Вывод: Deliver by sea in a container
