def get_age(name, ages):
    if name in ages:
        return ages[name]
    return "Not found"


get_name = input()
get_ages = eval(input())
print(get_age(get_name, get_ages))