# count = 100

# while count > 1:
#     count -= 1
#     if count == 1:
#         print("*" * 50)
#         print(f"{count} bottle of beer on the wall.")
#         print(f"{count} bottle of beer.")
#         print(f"Take one down, pass it around, no more bottels of beer on the wall")
#         print("*" * 50)
#     else:
#         print("*" * 50)
#         print(f"{count} bottles of beer on the wall.")
#         print(f"{count} bottles of beer.")
#         print(f"Take one down, pass it around, {count - 1} bottles of beer on the wall.")
#         print("*" * 50)


for num_bottles in range(99,0,-1):
    if num_bottles == 1:
        print("*" * 50)
        print(f"{num_bottles} bottle of beer on the wall.")
        print(f"{num_bottles} bottle of beer.")
        print(f"Take one down, pass it around, no more bottels of beer on the wall")
        print("*" * 50)
    else:
        print("*" * 50)
        print(f"{num_bottles} bottles of beer on the wall.")
        print(f"{num_bottles} bottles of beer.")
        print(f"Take one down, pass it around, {num_bottles - 1} bottles of beer on the wall.")
        print("*" * 50)