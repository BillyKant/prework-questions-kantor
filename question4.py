def is_leap_year(a_year):
    if a_year % 4 == 0 and a_year % 100 != 0 or a_year % 400 == 0:
        return True
    else:
        return False

print(is_leap_year(1700))
print(is_leap_year(1600))
print(is_leap_year(2020))