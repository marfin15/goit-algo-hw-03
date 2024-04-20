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
    if min < 1 or max > 1000 or quantity < 1 or quantity > (max - min + 1):
        return []
    lottery = random.sample(range (min, max), quantity)
    return sorted(lottery)

lottery_numbers = get_numbers_ticket(1, 100, 7)
print("Ваші лотерейні числа:", lottery_numbers)