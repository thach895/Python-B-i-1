class CoffeeOrder:
    vat_rate = 0.10

    def __init__(self, table_number):
        self.table_number = table_number
        self.__total_amount = 0

    @property
    def total_amount(self):
        return self.__total_amount

    def add_item(self, price):
        if price > 0:
            self.__total_amount += price

    def calculate_final_bill(self):
        return self.__total_amount * (1 + self.vat_rate)

    @classmethod
    def update_vat_rate(cls, new_rate):
        if 0 <= new_rate <= 1:
            cls.vat_rate = new_rate