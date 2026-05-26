# this file consists of python logic to debug code and chek that it works prior to recording it in the .md files

# Convert between c and f 
_choice = input("Would you like to input degrees in c or f: ")

if _choice == "c":
    _degrees_c = float(input("celsius degrees: "))
    _degrees_f = _degrees_c * (9/5) + 32
if _choice == "f":
    _degrees_f = float(input("fehrenheit degrees: "))
    _degrees_c = (_degrees_f - 32) / (9/5)

print(f"c: {_degrees_c}\nf: {_degrees_f}")