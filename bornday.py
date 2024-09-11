correct_birth_year = 1799

user_input_year = int(input("Введите год рождения А.С. Пушкина: "))

if user_input_year != correct_birth_year:
    print("Неверный год рождения")
else:
    user_input_day = int(input("Введите день рождения А.С. Пушкина: "))
    correct_birth_day = 6
    if user_input_day == correct_birth_day:
        print("Верно")
    else:
        print("Неверный день рождения")
