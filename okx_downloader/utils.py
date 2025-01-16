from datetime import datetime
import os

def validate_date_range(start_date: str, end_date: str):
    try:
        start = datetime.strptime(start_date, '%Y-%m-%d')
        end = datetime.strptime(end_date, '%Y-%m-%d')
        if start > end:
            raise ValueError("Начальная дата должна быть меньше или равна конечной дате.")
    except ValueError as e:
        raise ValueError(f"Ошибка проверки дат: {e}")

def sanitize_filename(filename: str) -> str:

    return filename.replace(' ', '_').replace('/', '_').replace('\\', '_')

def log_message(message: str):
    print(f"[LOG] {message}")
