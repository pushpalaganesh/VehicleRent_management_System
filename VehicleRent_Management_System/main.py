import vehicles_list


def index():
    print("======================//Rent/Hire a vehicle//====================")
    print("1.Car \n2.Bike \n3.Auto ")
    try:
        ip = int(input("Select the vehicle type: "))
        if ip == 1:
            print("The available list of cars are: ")
            vehicles_list.list_of_cars()
        elif ip == 2:
            print("The available list of bikes are: ")
            vehicles_list.list_of_bikes()
        elif ip == 3:
            vehicles_list.auto()
        else:
            print("You are selected invalid option")

    except Exception as e:
        print(e.args)


index()
