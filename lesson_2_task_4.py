fizz_buzz = input("Введите число: ")
num = float(fizz_buzz)

if (num%3 == 0) and (num%5 == 0):
    print("FizzBuzz")

elif (num%3 == 0):
    print("Fizz")

elif (num%5 == 0):
    print("Buzz")
    
else:
    print(num)