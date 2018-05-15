#This program generates a triangle using *
#CNA 336
#Wyatt Humphreys | wlhumphreys@studednt.rtc.edu


inputnum = int(input("Please enter an odd number "))

for i in range(inputnum): #Uses inputted number for range
    for x in range(i+1): #Range i+1 to find out how many * to print
        print("*",end="") #end="" is used to print on the same line
    print() #prints the *
for y in range(inputnum, 0, -1): #similar to line 8, except allows for triangle to print downward
    for z in range(y-1): #removes extra line from middle of triangle
        print("*",end="") #same process as line 10
    print() #prints the *