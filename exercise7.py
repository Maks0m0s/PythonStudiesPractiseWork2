from datetime import datetime
from collections import Counter

def plot_user_activity(dates):
    """
    Будує текстовий графік активності користувача за датами.

    Args:
        dates (list of str): Список дат у форматі "YYYY-MM-DD".
    """
    try:
        # Перетворюємо дати у формат datetime
        parsed_dates = [datetime.strptime(date, "%Y-%m-%d") for date in dates]

        # Підраховуємо кількість подій на кожну дату
        date_counts = Counter(parsed_dates)

        # Отримуємо унікальні дати та їх кількість у хронологічному порядку
        sorted_dates = sorted(date_counts.keys())
        counts = [date_counts[date] for date in sorted_dates]

        # Побудова текстового графіка
        print("\nАктивність користувача за датами:")
        for date, count in zip(sorted_dates, counts):
            print(f"{date.strftime('%Y-%m-%d')}: {'#' * count} ({count})")

    except Exception as e:
        print(f"Помилка: {e}")

# Приклад використання
date_list = [
    "2023-12-01", "2023-12-01", "2023-12-02",
    "2023-12-02", "2023-12-02", "2023-12-03"
]
plot_user_activity(date_list)
