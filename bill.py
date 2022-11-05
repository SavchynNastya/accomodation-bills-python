from functools import reduce


class Flatmate:
    def __init__(self, n, days):
        self.name = n
        self.days_in_house = days

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, val):
        if not isinstance(val, str):
            raise TypeError("Name should be a string")
        self.__name = val

    @property
    def days_in_house(self):
        return self.__days_in_house

    @days_in_house.setter
    def days_in_house(self, val):
        if not isinstance(val, int):
            raise TypeError("Days spent in house should be int")
        if val <= 0:
            raise ValueError("Days spent in house must be > 0")
        self.__days_in_house = val

    def how_many_pay(self, bill):
        if not isinstance(bill, Bill):
            raise TypeError("Bill must be an instance of Bill class")

        part = self.days_in_house / bill.total_days_in_house
        to_pay = bill.amount * part
        return round(to_pay, 2)


class Bill:
    def __init__(self, period, amount):
        self.period = period
        self.amount = amount
        self.total_days_in_house = 0

    @property
    def period(self):
        return self.__period

    @period.setter
    def period(self, val):
        if not isinstance(val, str):
            raise TypeError("Period should be a string (e.g 'December 2022')")
        if not val.split():
            raise ValueError("You should enter a month and a year")

        months = ("January", "February", "March", "April", "May", "June", "July",
                  "August", "September", "October", "November", "December")

        month, year = val.split()
        if month not in months:
            raise ValueError("Wrong month passed!")
        if not int(year):
            raise TypeError("Year should be an integer")
        year = int(year)

        self.__period = val

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, val):
        if not isinstance(val, int | float):
            raise TypeError("Accommodation pricing should be int or float")
        if val <= 0:
            raise ValueError("Accommodation pricing must be > 0")
        self.__amount = val

    def get_total_days(self, *flatmates):
        if any(not isinstance(flatmate, Flatmate) for flatmate in flatmates):
            raise TypeError("Flatmate must be an instance of Flatmate class")

        self.total_days_in_house = reduce(lambda days, mate: days + mate.days_in_house, flatmates,
                                          self.total_days_in_house)
