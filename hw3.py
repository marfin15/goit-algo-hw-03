from datetime import datetime

def get_days_from_today(date):
    try:
        input_date = datetime.strptime(date, '%Y-%m-%d')
        today = datetime.today()
        difference = today - input_date
        return difference.days
    except ValueError:
        return "Введено не вірний формат дати."
print(get_days_from_today("2024-02-24"))