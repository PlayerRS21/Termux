lst =[9,7,10,4,6,2,3]

lstNew=[]

"""
def gs():
    S=lst[0]
    for i in lst:
        if S>i:
            S=i
#        print(S)
    lstNew.append(S)
    lst.remove(S)
#    print(lst)
"""
def ass():
    def gs():
        S=lst[0]
        for i in lst:
            if S>i:
                S=i
            #print(S)
        lstNew.append(S)
        lst.remove(S)
        #print(lst)

    x=0
    z=len(lst)
    while (x<z):
        gs()
        x=x+1
    
#    lstNew.append(lst[0])

#print(lstNew)



ass()

print(lstNew)
