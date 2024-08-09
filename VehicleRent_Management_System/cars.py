class Thar:
    def price(self):
        print("1.3500/1hr\n2.1day/12000 \n3.50000/month")
        rental_type = int(input("Select your option: "))
        if rental_type == 1:
            hrs = int(input("How many hours do you want: "))
            print("You have to pay: ", hrs * 3500)
        elif rental_type == 2:
            days = int(input("How many days do you want: "))
            print("You have to pay: ", days * 12000)
        else:
            print("You are selected invalid option")


class XUV(Thar):
    pass


class Scorpio(Thar):
    pass


class Defender(Thar):
    pass

