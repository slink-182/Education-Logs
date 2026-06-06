# first python file on bean

def CallNameVar():
    name = "jeremy"
    print(name)
# CallNameVar()

def AfterTything(income):
    return income*.9

def main():
    income = float(input("input income: "))
    print(f"your remainder after tything is {AfterTything(income)}")
# main()

def ForLoopFunc():
    for i in range(1,11):
        print(i)
        # i+=1
# ForLoopFunc()

def ForLoopTwo():
    i = 0
    while i < 10:
        print(i)
        i += 1
    print(i)
# ForLoopTwo()

def ChooseIfStates():
    while (True):
        number = int(input("input number: "))

        if number < 10:
            print("number is less than 10.")
        elif number == 10:
            print("number is equal to 10.")
        elif number > 10 and number != 67:
            print("number is greater than 10.")
        elif number == 67:
            print("of course you chose this number you fawking retardation of human fecal matter you incel prick. Love you<3")
            break
# ChooseIfStates()

def NestedForLoop():
    numbers = range(1,11)
    numbers2 = range(1,11)
    for i in numbers:
        for j in numbers2:
            print(j)
# NestedForLoop()

def MoreLoops():
    numbers = range(1,11)
    for i in numbers:
        print(i)
    for j in numbers:
        j*=2
        print(j)
# MoreLoops()

def AnotherLoop():
    number = 0
    while(True):
        if number < 2:
            number +=1
            print(number)
        if number > 1:
            number *= number
            print(number)
        if number > 10000:
            break    
# AnotherLoop()

# this func runs under the assumption that deposits are made at the start of the year.
def CompoundInterest():
    time = 0
    savings = 0
    totalInvestedIncome = 0
    deposit = float(input("per year deposit into savings: "))
    while (True):
        totalInvestedIncome += deposit
        savings += deposit
        savings *= 1.09
        time += 1
        if time == 30:
            gain = savings - totalInvestedIncome
            print(f"invested income: ${totalInvestedIncome:,.2f}\ntotal return: ${savings:,.2f}\nmoney gained: ${gain:,.2f}")
            break
CompoundInterest()