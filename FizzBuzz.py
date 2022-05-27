for num in range(1, 101):
    string = ''

    # ここから記述
    if num % 15 == 0:
        print("FizzBuzz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0:
        print("Fizz")
    else:
        print(num)

    # ここまで記述

    print(string)
