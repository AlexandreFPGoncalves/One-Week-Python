 ## [One Week Python Course](https://www.udemy.com/course/one-week-python/)

## Project Resume

</br>

##### Integers and Floats

```sh
File: Section3_PythonNumbers/integersAndFloats.py
```

-   <b>Integers</b> are numbers with <b>no decimal</b> houses like the following examples
-   While <b>Floats</b> may be rounded but <b>always have a decimal house</b>
-   The method <b>type()</b> is used to reveal the type of the argument used

```py
type(5)     //<class "int">
type(5.0)   //<class "float">
```

</br>

##### Basic Operators

```sh
File: Section3_PythonNumbers/basicOperators.py
```
-   If you calculate an integer and a float <b>the answer will always be a float</b>

```py
print("Type of 12 + 1.5",type(12+1.5))    #Type of 12 + 1.5 <class 'float'>
```
##### Integer Division
-   It rounds down the result
```py
print("10 / 3 = ", 10 / 3, " | 10 // 3 = ", 10 // 3)    
#10 / 3 =  3.3333333333333335 | 10 // 3 =  3
```
##### Exponentiation
```py
print("8 ** 3 = ", 8 ** 3)    
#8 ** 3 =  512
```

##### Modulo
-   Remainder of the operation
```py
print(38 % 10) 
# 10 goes into 38... 3 times, with a remainder of 8
```

##### Basic Operators

##### len
-   length of a string
```py
name = "Alex"
len(name) #4
```

##### input
-   Inputs a question to the user and can be captured in a variable
```py
first_name = input("What is your name?")
print("So your name is " + first_name+ "!")
#So your name is XXX!
```

##### Casting Typess
-   They change the variable type, int will chop the float decimal off

```py
age = input("How old are you?")
doubled_age = int(age) * 2
print("if we multiplied your age by 2 it would be: " + str(doubled_age))
#How old are you?20
#if we multiplied your age by 2 it would be: 40
```

##### FStrings
-   f strings will read and evaluate and code between {} the result will be turned into a string and inserted into the overall string

```py
age_in_days = input("How old are you? (in days (years*365))")
print(f"You are {float(age_in_days) / 365} old!")
#How old are you? (in days (years*365))7665
#You are 21.0 old!
```

##### Comparison Operators 

##### Comparing Floats and Ints
-   if you compare float and ints they represent the same value

```py
print(4.00000 == 4)
#True
print(4.00001 == 4)
#False
```

##### The "in" Operator
-  The "in" operator looks to see if an items is a member of a sequence.

```py
"a" in "cat"
#True
```

##### Generate random int

```py
from random import randint
print(randint(1,6))
```