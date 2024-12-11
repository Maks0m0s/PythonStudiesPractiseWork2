from datetime import datetime

def calculate_age(birth_date):
    """
    Обчислює вік у днях, місяцях і роках на основі дати народження.

    Args:
        birth_date (str): Дата народження у форматі "YYYY-MM-DD".

    Returns:
        dict: Словник з віком у роках, місяцях та днях.
    """
    try:
        # Перетворюємо дату народження у форматі "YYYY-MM-DD" на об'єкт datetime
        birth_date = datetime.strptime(birth_date, "%Y-%m-%d")
        current_date = datetime.now()

        # Перевіряємо, чи дата народження у майбутньому
        if birth_date > current_date:
            raise ValueError("Дата народження не може бути у майбутньому.")

        # Різниця у роках
        years = current_date.year - birth_date.year

        # Різниця у місяцях
        months = current_date.month - birth_date.month
        if months < 0:
            years -= 1
            months += 12

        # Різниця у днях
        days = current_date.day - birth_date.day
        if days < 0:
            months -= 1
            if months < 0:
                years -= 1
                months += 11
            previous_month = (current_date.month - 1) if current_date.month > 1 else 12
            previous_month_year = current_date.year if current_date.month > 1 else current_date.year - 1
            days_in_previous_month = (datetime(previous_month_year, previous_month + 1, 1) - datetime(previous_month_year, previous_month, 1)).days
            days += days_in_previous_month

        return {
            "years": years,
            "months": months,
            "days": days
        }

    except ValueError as e:
        return {"error": str(e)}

# Приклад використання
birth_date_input = "2010-02-15"
result = calculate_age(birth_date_input)
if "error" in result:
    print("Помилка:", result["error"])
else:
    print(f"Вік: {result['years']} років, {result['months']} місяців, {result['days']} днів.")
