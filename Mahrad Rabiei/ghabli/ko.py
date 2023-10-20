# print('Az 1 ta 5 entekhab ?')

# while True:
#     try:
#         num = int(input("--->"))
#         if num in range(1, 6):
#             if num > 5:
#                 print("dari ghalat mizani")
#             break
#     except ValueError:
#         print("dari eshtebah mizani")
#

# i = int
# for _ in range(1, 5):
#     i = int(input("sahih"))
#     if i not in range(1, 5):
#         print("wrong")



# i = 0
# while i in range(1, 5):
#     i = int(input("--->"))



# number = int(input("--->"))
#
# while number < 1 or number > 5:
#     print("dari eshtebah mizani")
#     number = int(input("please between 1 to 5: "))
#
#     print("adadi ke zadi", number)
#



# while True:
#     try:
#         number = int(input("--->"))
#         if number < 1 or number > 5:
#         print("dari eshtebah mizani")
#     else:
#     break
#     exept ValueError:
#     print("please between 1 to 5")
#     print("adadi ke zadi", number)

# ---------------------------------------------------------------------

print('Az 1 ta 5 entekhab ?')

numbers = []

while True:
    try:
        num = int(input("--->"))
        if num < 1 or num > 5:
            print("please between 1 to 5")
            continue
        numbers.append(num)
    except ValueError:
        print("wrong")
    else:
        break
if num == 1:
    (num*2)
elif num == 2:
    (num*3)
elif num == 3:
    (num*4)
elif num == 4:
    (num*5)
elif num == 5:
    (num*6)
else:
    print()

print("your number", numbers)

# if num == 1:
#     print(num*2)
























































