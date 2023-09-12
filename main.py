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
    print("Введите число пожалуйста")
except Exception as error:
    print(f"Error: {error}")


