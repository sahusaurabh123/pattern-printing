# n=int(input(print("Enter a number")))
# # b=int(input("Enter '1' or '0'"))
#
# for i in range(1,n+1):
#     print(i*"*")

while(True):
    num1=int(input(print("Enter no.of rows")))
    bool=bool(int(input(print("Enter 1 for 'true' or 0 for 'false'"))))

    if bool==True:
        print("You have choosen '1' so it is true")
        for i in range(1,(num1+1),1):
            print(i*"*")
        break
    else:
        print("You have choosen '0' so it is false")
        for j in range(num1,0,-1):
            print(j*"*")
        break



