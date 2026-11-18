class Medicine:
    def __init__(
            self,
            price = 0.0,
            quantity = 0,
            name = "Trenbolon",
            is_prescription_needed = False,
            expiration_date = "2027-01-01",
    ):
            self.quantity = quantity
            self.price = price
            self.name = name
            self.is_prescription_needed = is_prescription_needed
            self.expiration_date = expiration_date

    def __del__(self):
        print(f"Medicine {self.name} deleted")

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name


class Pharmacy:
    def __init__(self):
        self.medicines = []

    def add_medicine(self, medicine):
        self.medicines.append(medicine)

    def __del__(self):
        print("Pharmacy closed")

    def remove_medicine(self, name):
        self.medicines = [medicine for medicine in self.medicines if medicine.name != name]

    def remove_expired(self, current_date):
        self.medicines = [medicine for medicine in self.medicines if medicine.expiration_date >= current_date]

    def apply_discount(self):
        for medicine in self.medicines:
            medicine.price = medicine.price * 0.9

    def get_cheapest_medicine(self):
        if not self.medicines:
            print("В аптеці немає ліків")
            return []
        min_price = min(medicine.price for medicine in self.medicines)
        cheapest = [medicine for medicine in self.medicines if medicine.price == min_price]
        return cheapest


if __name__ == "__main__":
    pharmacy = Pharmacy()

    med1 = Medicine(price=150.0, quantity=10, name="Aspirin", is_prescription_needed=False, expiration_date="2027-05-01")
    med2 = Medicine(price=50.0, quantity=25, name="Paracetamol", is_prescription_needed=False,expiration_date="2025-01-01")
    med3 = Medicine(price=50.0, quantity=5, name="Analgin", is_prescription_needed=False,expiration_date="2028-10-10")

    pharmacy.add_medicine(med1)
    pharmacy.add_medicine(med2)
    pharmacy.add_medicine(med3)

    print("--- АСОРТИМЕНТ ПІСЛЯ ДОДАВАННЯ ---")
    for m in pharmacy.medicines:
        print(f"Залишились: {m.name}, Термін: {m.expiration_date}")

    pharmacy.apply_discount()
    print("\n--- ПІСЛЯ ЗНИЖКИ 10% ---")
    for m in pharmacy.medicines:
        print(f"Ліки: {m.name}, Нова ціна: {m.price}")

    cheapest_list = pharmacy.get_cheapest_medicine()
    print("\n--- НАЙДЕШЕВШІ ЛІКИ ---")
    for m in cheapest_list:
        print(f"Назва: {m.name}, Ціна: {m.price}")

    pharmacy.remove_medicine("Aspirin")
    print("\n--- ПІСЛЯ ВИДАЛЕННЯ Aspirin ЗА НАЗВОЮ ---")
    for m in pharmacy.medicines:
        print(f"Залиитись на складі: {m.name}")


class Vertolit:
    def __init__(self, name, price)
        self.__name = name
        self.price = price

    def get__name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name


@property
def class_name(self):








