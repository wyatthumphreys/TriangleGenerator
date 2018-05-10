inputnum = int(input("Please enter an odd number "))

for i in range(0,inputnum): #Numbers between the first line and the user inputted number
    for x in range(0,i+1): #Arrays start at 0. Range between 0 and the first variable (i) minus 1 to find out how many * to print
        print("*",end="") #end=" " is used to print on the same line
    print() #prints the *