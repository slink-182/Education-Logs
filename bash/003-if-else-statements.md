# 003 IF ELSE STATEMENTS

after learning how to make variables and operators to compare them, it is now time to learn if and else statements.
The basic fundamental example of an if statement is as follows:

```bash
arg1=12

if [ "$arg1" -eq 12 ]; then
    echo "the two values are of the equal value of 12"
else
    echo "the values are not equal."
fi
```
It is also general procedure to encapsulate variables as follows:
```bash
if [ "$variable1" -lt "$variable2" ]; then
    echo "var1 is less than var2."
fi
```
another example
```bash
if [ "$men" -eq "$women" ]; then
    echo "these are variables containing equal value."
fi
```