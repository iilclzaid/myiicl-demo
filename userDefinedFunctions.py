# Functions : A reusebale block of code created to perform certain task without redundant technique

# Declaration of functions
#def :- define
def calcSum(a,b):  #Declaration of Parameters
    add = a + b
    # print("Addition is",add)
    return add

print(calcSum(52,42))  # Passing an arguments

def calcAverage(n):
    if(n > 18):
        pass
    else:
        print("Your age is ",n,end=" ")
        print("You cannot vote")
calcAverage(12)


def printName(my_name="Kazi"):
    print("My Name is ",my_name)

printName("Mahesh")
printName()

# Neon Number : 9  9*9 = 81   8+1 = 9

num = int(input("Enter Your Number"))
def neonNumber(num):
        square = num * num
        sum=0
        while(square >0):
            rem = square %10
            sum = sum+rem
            square= square//10
        if(sum == num):
            print("Neon Number")
        else:
            print("Not a Neon Number") 
neonNumber(num)

#  Star Pattern

def starPattern(num):
    for i in range(1,num):
        for j in range(1,i+1):
            print("*",end="")
        print()
starPattern(5)

#  Krishna Murthy Number (145 = 1+24+120 = 145)  
def krishnaNumber(num):
    rem=0
    store =0
    temo=num
    while(num > 0):
        i=1
        rem = num%10  #5  4
        fact=1
        while(i<=rem): 
            fact = fact*i #120
            i+=1
        store = store + fact
        num = num //10
    
    if(store ==temo):
        print("Krishna Number")
    else:
        print("Not a Krishna Number")

krishnaNumber(145)