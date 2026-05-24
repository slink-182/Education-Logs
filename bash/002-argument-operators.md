# 002 ARGUMENT OPERATORS

Before we delve into the world of if, else, while, and for statements, we need an understanding of general operators for comparisons. The following is a list of general purpose comparison operators used between two arguments

## Numeric Comparisons

argument 1 is equal to argument 2
```bash
[ arg1 -eq arg2 ]
```
argument 1 is not equal to argument 2
```bash
[ arg1 -ne arg2 ]
```
argument 1 is less than argument 2
```bash
[ arg1 -lt arg2 ]
```
argument 1 is less than or equal to argument 2
```bash
[ arg1 -le arg2 ]
```
argument 1 is greater than argument 2
```bash
[ arg1 -gt arg2 ]
```
argument 1 is greater than or equal to argument 2
```bash
[ arg1 -ge arg2 ]
```

## String Comparisons

argument 1 is equal to argument 2
```bash
[ arg1 = arg2 ]
```
argument 1 is not equal to argument 2
```bash
[ arg1 != arg2 ]
```

```bash
-f  # is a regular file
-d  # is a directory
-e  # exists
-r  # readable
-w  # writable
-x  # executable
```

the following section will break down if statements with comparisons, but here is an example to start:
```bash
age=67
# if age is greater than or equal to 18, print "adult" otherwise, print "minor"
if [ "$age" -ge 18 ]; then
    echo "adult"
else
    echo "minor"
fi
```

## NOTE
When writing arguments, remember to have spaces on both sides of the brackets like the following examples:
```bash
# arg 1 is equal to arg 2, or arg 1 is greater than arg 2
if [ arg1 -eq arg2 ] || [[ arg1 -gt arg2 ]]
```
In this case, we see space between the word "if" and the first enter bracket. We also see space between the first enter bracket and the name of the first argument. The || is used in this example to express "or". Also notice that double brackets do work if preferred. Also -- remember to use the dollar sign to grab variable names: 
```bash
if [ $age -gt 200 ]; then
echo "you are old"
fi
```
