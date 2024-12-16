is_year_leap = int(input("Введите год: "))

if (is_year_leap % 4 == 0):
    result = "True"
else:
    result = "False"

print(f"год{is_year_leap}: {result}")