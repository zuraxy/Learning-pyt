numbers = 0
while (numbers<100):
    numbers += 1
    if (numbers%15 == 0):
        print("FizzBuzz")
        continue
    if (numbers%3 == 0):
        print("Fizz")
        continue
    if (numbers%5 == 0):
        print("Buzz")
        continue
    print (numbers)
    if (numbers%2 == 1) and (numbers%3 == 1 or 2) and (numbers%5 == 1 or 2 or 3 or 4) and (numbers%7 == 1 or 2 or 3 or 4 or 5 or 6):
            print("prime")