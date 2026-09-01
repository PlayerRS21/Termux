lst=[]
lstCopy=lst.copy()
lstNew = []

def input_taker():
    while True:
        n = input("Enter a Number or press enter to move forward: ")

        try:
            n=int(n)
            lst.append(n)
        except:
            if n=="":
                do()
                break
            else:
                print("Invalid Input Captured")

def gs(a):
    if a =="s":
        S=lst[0]
        for i in lst:
            if S>i:
                S=i
        lstNew.append(S)
        lst.remove(S)
    elif a =="g":
        G=lst[0]
        for i in lst:
            if G<i:
                G=i
        lstNew.append(G)
        lst.remove(G)

def ass():
    z=len(lst)
    x=0
    while (x<z):
        gs("s")
        x=x+1

def des():
    z=len(lst)
    x=0
    while(x<z):
        gs("g")
        x=x+1

def do():
    a = input("What you want to do\n1. Accending Order(1)\n2. Decending Order(2)\n--> ")
    if a=="1":
        print("Assending Order Will Be: ")
        ass()
        print(lstNew)
    elif a=="2":
        print("Decending Order Will Be: ")
        des()
        print(lstNew)
    else:
        print("Wrong Input Detected.\n")
        do()

input_taker()
