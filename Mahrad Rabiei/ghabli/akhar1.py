# lotfan be soalat az 1 ta 5 pasokh bedid

# question_tuple = ('حالت چطوره ؟', 'چقدر از تنهایی لذت میبری ؟', 'میزان قوی بودن ارتباط شما با آدم ها ؟')
# print(question_tuple[::3])


# def get_coefficients(num_of_questions):
#     coefficients = []
#     for i in range(num_of_questions):
#         coefficient = float(input(f"Enter coefficients {i+1}: "))
#         coefficients.append(coefficient)
#         return coefficient
#


# num_of_questions = int(input("enter the number of questions: "))
# coefficients = get_coefficients(num_of_questions)
# print(coefficients)
#

def multiply_list_elements():
    input_list = input("enter a list of numbers, separated by spaces: ").split()
    input_list = [int(x) for x in input_list]

    factor = int(input("enter a factor: "))

    result_list = []
    for num in input_list:
        result_list.append(num*factor)

    return result_list


print(multiply_list_elements())


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

print("your number", numbers)
