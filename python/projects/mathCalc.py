
def Q1():
    x = 10
    y = "10"

    print(x + int(y))

'''
predict: values x and y will add together. despite y being a string, 
the use of keyword "int" within the print statement converts it the 
same datatype allowing it to be used for mathematics.

conclusion: yes, my logic was correct.
'''

def Q2():
    a = "123"
    b = int(a)
    print(b + 2)

    '''
    output: 123+2 = 125;
    a stores number as a string, and then b represents that number as an int.
    b + 2 is just intValue + 2.
    '''

# Q2()

def Q3():
    numberList = range(1,5)
    sqrs = [i*i for i in numberList]
    print(sqrs)
    


# run each question/problem
def main():
    while (True):    
        c = input("select Q\n: ")
        c = c.isdigit()
        if not c.isdigit():
            print("Number must be int!") 
        else:
            c = c.isdigit()
            if c == 0:
                print("Have a great day!")
                break
            elif c == 1:
                Q1()
            elif c == 2:
                Q2()
            elif c == 3:
                Q3()


main()