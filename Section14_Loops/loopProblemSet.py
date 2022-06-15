
#  ----------
#    PART 1
#  ----------
word = "supercalifragilisticexpialidocious"

# Write a for loop that prints out each character in the above "word" variable
for char in word:
    print(char)

# Write a while loop that does the same thing!
count = 0
while count < len(word):
    print(word[count])
    count += 1
   

#  ----------
#    PART 2
#  ----------
# Write a while loop that prints the even numbers from 100 to 140 (including 140)
num = 100
while num <= 140:
    print(num)
    num += 2

# Write a for loop that does the same thing (with range())
for evenNumbers in range(100,142,2):
    print(evenNumbers)

#  ----------
#    PART 3
#  ----------
# Write a loop that asks a user to input the passphrase "sillygoose" and keeps asking them to do so until they comply:
userPhrase = input('Please type "sillygoose": ')

while userPhrase != "sillygoose":
    userPhrase = input('that is not it! Please do type "sillygoose": ')

print("U got it you Silly Goose!")