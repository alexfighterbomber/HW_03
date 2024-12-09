from datetime import datetime

def get_days_from_today(date: str):                  # розрахунок кількості днів між date та поточною датою
    current_date = datetime.today().date()
    try:
        target_date = datetime.strptime(date, "%Y-%m-%d").date()   # рядок в формат datetime
    except ValueError:
        return 'Невірний формат дати. Використовуйте "РРРР-ММ-ДД"'
    return (current_date - target_date).days

print(get_days_from_today("2024-12-06"))