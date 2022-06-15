from random import randint

dice1 = randint(1,6)
dice2 = randint(1,6)
counterRolls = 1;

while dice1 != 1 or dice2 != 1:
    print(dice1, dice2)
    dice1 = randint(1,6)
    dice2 = randint(1,6)
    counterRolls += 1


print("Test",dice1, dice2)
print(f"Hey you got Snake eyes! and it only took you {counterRolls} rolls")
