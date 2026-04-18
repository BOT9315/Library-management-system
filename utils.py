from datetime import datetime

books = {}
next_id = 1
issued_books = {}
returned_books = {}


def calculate_fine(days_late):
    if days_late <= 0:
        return 0
    fine = 0
    remaining = days_late
    week = 1
    rate = 10           # Rs.10/day for week 1
    while remaining > 0:
        days_in_week = min(7, remaining)
        fine = fine  + (days_in_week * rate)
        remaining = remaining - days_in_week
        week = week + 1
        rate = rate * week    # week2 -> 20/day, week3 -> 60/day ...
    return fine
