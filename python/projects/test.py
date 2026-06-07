# this file consists of python logic to debug code and chek that it works prior to recording it in the .md files

LINE_BREAKS = 44

# list of functios to call
def main():
    while (True):
        c = int(input(f"{"-"*LINE_BREAKS}\nchoose function\n| 1. TempConversion\n| 2. NumberScrape\n| 3. NestedLoopTest\n| 4. BasicIf\n| 5. quit\n: "))
        if c == 1:
            TempConversion()
        elif c == 2:
            NumberScrape()
        elif c == 3:
            NestedLoopTest()
        elif c == 4:
            BasicIf()
        elif c == 5:
            break
        elif c > 5 or c < 1 :
            print("Choose a number between 1 and 5.")

def TempConversion():
# Convert between c and f 
    _choice = input("Would you like to input degrees in c or f: ")

    if _choice == "c":
        _degrees_c = float(input("celsius degrees: "))
        _degrees_f = _degrees_c * (9/5) + 32
    if _choice == "f":
        _degrees_f = float(input("fehrenheit degrees: "))
        _degrees_c = (_degrees_f - 32) / (9/5)

    print(f"c: {_degrees_c}\nf: {_degrees_f}")

def NumberScrape():
    text = "this is a random setence containing numbers: 1234 5678"
    numbers = []

    for char in text:
        if char.isdigit():
            numbers.append(int(char))

    print(numbers)

def NestedLoopTest():
    for i in range(3):
        '''in range, will not include the number listed. So a range of 3 will max at 2.'''
        for j in range(3):
            '''with each number in range, starting from 0, follow the same range but if i is equal to j, dont include.'''
            if i == j:
                break
            print(i, j)
'''
potential numbers for the outer loop are 0,1,2.
i = 0 and j = 0 break
i = 1 and j = 0 print
i = 2 and j = 0 print
i = 2 and j = 1 print

Cannot print if same value.
'''

def BasicIf():
    x = 10
    if x < 5:
        print("low")
    else:
        print("high")
'''
this will print high<3
'''

# call main to select other functions!
main()