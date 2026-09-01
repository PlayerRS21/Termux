users = {
    1:{
        "userName":"Ritesh",
        "accountType":"FuckingInsane",
        "remainingBalance": 2000
    },
    12:{
        "userName":"Rahul",
        "accountType":"SavingsAccount",
        "remainingBalance": 20
    },
    10:{
        "userName":"Sam",
        "accountType":"SavingsAccount",
        "remainingBalance": 20
    },
    20:{
        "userName":"Devil",
        "accountType":"BusinessAccount",
        "remainingBalance": 1000000
    }

}


class Bank:
    
    __verified = False

    def __init__(self, accountNum, name):
        self.name = name
        self.__accountNumber = accountNum
        self.__verifyUser(self.__accountNumber,self.name)

    def __verifyUser(self,accNum,name):
        try:
            if (accNum in users) & (users[self.__accountNumber]["userName"] == name):
                self.__verified = True
                # print(self.__verified)
            else:
                self.__verified = False
                # print(self.__verified)
        except KeyError:
            return 0

    def checkBalance(self):
        if (self.__verified == True):
            # print("Your Current Balance is: ",self.__accountNumber["remainingBalance"])/
            return users[self.__accountNumber]["remainingBalance"]
        else:
            return "Not Verified."

    def transferAmount(self,amount):
        if (self.__verified == True):
            if(users[self.__accountNumber]["remainingBalance"]>amount):
                print("Payment Done.")
            else:
                print("Insufficient Balance")
        else:
            print("Invalid Credentials")

    # RequestMoney
    # History
    # Add User


u1 = Bank(1,"Ritesh")

u1.transferAmount(10)

# print(u1.checkBalance())

# u1.verifyUser(1, "Ritesh")

# u1.transferAmount(1000)
# print(u1.checkBalance())
