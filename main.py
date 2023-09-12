try:
    user_choice_day = int(input("Введите номер дня недели "))

    match user_choice_day:
        case 1:
            print("Понедельник")
        case 2:
            print("Вторник")
        case 3:
            print("Среда")
        case 4:
            print("Четверг")
        case 5:
            print("Пятница")
        case 6:
            print("Суббота")
        case 7:
            print("Воскресенье")
        case _:
            raise Exception("Пожалуйста введите корректный номер дня недели ")
except ValueError as error:
    print("Введите число пожалуйста ")
except Exception as error:
    print(f"Error: {error}")


############################
try:
    user_number_1, user_number_2 = int(input("Ваше первое число ")), int(input("Ваше второе число "))

    if user_number_1 == user_number_2:
        print("Числа равны")
    elif user_number_1 > user_number_2:
        print(user_number_2, user_number_1)
    elif user_number_2 > user_number_1:
        print(user_number_1, user_number_2)

except ValueError as error:
    print("Введите числовые данные")
except Exception as error:
    print(f"Error: {error}")

try:
    first_user_number = int(input("Ваше первое число "))
    second_user_number = int(input("Ваше второе число "))

    ongoing_operation = input("Пожвлуйста выберите операцию из предложеных - (+, -, *, /) ")
    match ongoing_operation:
        case "*":
            print(first_user_number * second_user_number)
        case "/":
            print(first_user_number / second_user_number)
        case "+":
            print(first_user_number + second_user_number)
        case "-":
            print(first_user_number - second_user_number)
        case _:
            print("Выберите математическую операцию из предложенных")

except ValueError as error:
    print("Выберите числовые данные")
except Exception as error:
    print(f"Error: {error}")
