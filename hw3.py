from datetime import datetime

def get_days_from_today(date):
    try:
        input_date = datetime.strptime(date, '%Y-%m-%d')
        today = datetime.today()
        difference = today - input_date
        return difference.days
    except ValueError:
        return "Введено не вірний формат дати."
print(get_days_from_today("2024-02-23"))


# **************************************************


import random

def get_numbers_ticket(min, max, quantity):
    lottery = random.sample(range (min, max), quantity)
    print(f"Ваші лотерейні числа: {sorted(lottery)}")

get_numbers_ticket(1, 10, 3)