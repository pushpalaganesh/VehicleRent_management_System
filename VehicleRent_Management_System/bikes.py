class Scooty:
    def price(self):
        print("1.300/1hr\n 2.1day/1000")
        rental_type = int(input("Select your option: "))
        if rental_type == 1:
            hrs = int(input("How many hours do you want: "))
            print("You have to pay: ", hrs * 300)
        elif rental_type == 2:
            days = int(input("How many days do you want: "))
            print("You have to pay: ", days * 1000)
        else:
            print("You are selected invalid option")


class Ola_electric:
    def e_price(self):
        print("1.150/1hr\n2.500/1day")
        rental_type = int(input("Select your option: "))
        if rental_type == 1:
            hrs = int(input("How many hours do you want: "))
            print("You have to pay: ", hrs * 150)
        elif rental_type == 2:
            days = int(input("How many days: "))
            print("You have to pay: ", days * 500)
        else:
            print("You are selected invalid option")


class RE_standard_350:
    def rePrice(self):
        print("1.900/1hr\n2.5000/1day")
        rental_type = int(input("Select your option: "))
        if rental_type == 1:
            hrs = int(input("How many hours do you want: "))
            print("You have to pay: ", hrs * 900)
        elif rental_type == 2:
            days = int(input("How many days do you want: "))
            print("You have to pay: ", days * 5000)
        else:
            print("You are selected invalid option")


class RX100:
    def rxprice(self):
        print("1.100/1hr\n2.600/1day")
        rental_type = int(input("Select your option: "))
        if rental_type == 1:
            hrs = int(input("How many hours do you want: "))
            print("You have to pay: ", hrs * 100)
        elif rental_type == 2:
            days = int(input("How many days do you want: "))
            print("You have to pay: ", days * 600)
        else:
            print("You are selected invalid option")
