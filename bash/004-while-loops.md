# 004 WHILE LOOPS

While loops are incredibly useful for repeating functions. The following example runs a hot to cold game until the user inputs the correct number 22:

```bash
while (true); do
    read -p "input a number: " x
    if [ $x -eq 22 ]; then
        echo "bingo!"
        break
    elif [ $x -lt 22 ]; then
        echo "higher!"
    elif [ $x -gt 22 ]; then
        echo "lower!"
    fi
done
```

Lets break down what this file is doing:

```bash
# while said attribute is met, run the following code
while (true); do
# ask for user input and store it in the variable x
    read -p "input a number: " x
# if x is equal to 22, run echo "bingo" and break out of the while loop and end the program
    if [ $x -eq 22 ]; then
        echo "bingo!"
        break
# also check to see if x is less than 22 and echo "higher!"
    elif [ $x -lt 22 ]; then
        echo "higher!"
# also check if x is greater than 2 and echo "lower!"
    elif [ $x -gt 22 ]; then
        echo "lower!"
    fi
done
```