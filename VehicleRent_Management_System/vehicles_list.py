from cars import Thar, Defender, XUV, Scorpio
from bikes import Scooty, Ola_electric, RE_standard_350, RX100
from auto import CNG,Electric


def list_of_cars():
    print("1.Thar \n2.XUV \n3.Scorpio \n4.Defender ")
    ctype = int(input("Select your option: "))
    if ctype == 1:
        Thar().price()
    elif ctype == 2:
        XUV().price()
    elif ctype == 3:
        Scorpio().price()
    elif ctype == 4:
        Defender().price()
    else:
        print("You are selected invalid option")


def list_of_bikes():
    print("1.Scooty \n2.Ola electric \n3.RE standard 350 \n4.RX100 ")
    btype = int(input("Select your option: "))
    if btype == 1:
        Scooty().price()
    elif btype == 2:
        Ola_electric().e_price()
    elif btype == 3:
        RE_standard_350().rePrice()
    elif btype == 4:
        RX100().rxprice()
    else:
        print("You are selected invalid option")


def auto():
    print("1.CNG \n2.Electric ")
    atype = int(input("Select your option: "))
    if atype == 1:
        CNG().price()
    elif atype == 2:
        Electric().e_price()
    else:
        print("You are selected invalid option")
