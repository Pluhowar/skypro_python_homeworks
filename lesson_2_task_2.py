is_year_leap = input()
year_number = int(is_year_leap)

if (year_number % 4 == 0):
    result = "True"
else:
    result = "False"

print("год " + is_year_leap + " " + result)