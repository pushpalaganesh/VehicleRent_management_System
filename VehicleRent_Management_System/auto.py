class CNG:
    def price(self):
        print("1.500/day \n2.13000/month")
        a_type = int(input("Select your option: "))
        if a_type == 1:
            days = int(input("How many days do you want: "))
            print("You have to pay: ",days*500 )
        elif a_type == 2:
            months = int(input("How many months do you want: "))
            print("You have to pay: ", months*13000)
        else:
            print("You are selected invalid option")


class Electric:
    def e_price(self):
        print("1.300/day\n2.3000/month")
        a_type = int(input("Select your option: "))
        if a_type == 1:
            days = int(input("How  many days do you want: "))
            print("You have to pay: ", days*300)
        elif a_type == 2:
            months = int(input("How many months do you want: "))
            print("You have to pay: ", months*3000)
        else:
            print("You are selected invalid option")
