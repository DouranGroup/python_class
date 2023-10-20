# lotfan be soalat az 1 ta 5 pasokh bedid

question_tuple = ('حالت چطوره ؟', 'چقدر از تنهایی لذت میبری ؟', 'میزان قوی بودن ارتباط شما با آدم ها ؟')
print(question_tuple[::3])

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
    print(num * 2)
elif num == 2:
    (num * 3)
elif num == 3:
    (num * 4)
elif num == 4:
    (num * 5)
elif num == 5:
    (num * 6)
else:
    print()

print("your number", numbers)

