from datetime import timedelta, datetime

from libs.get_days_from_today import get_days_from_today
from libs.get_numbers_ticket import get_numbers_ticket
from libs.get_upcoming_birthdays import date_format, get_upcoming_birthdays
from libs.normalize_phone import normalize_phone

days = get_days_from_today('2022-02-24')
print(f"From today: {days} day(s)", "\n")

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Your lottery numbers:", lottery_numbers, "\n")

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Normalized phone numbers for sending SMS:", sanitized_numbers, "\n")

today = datetime.today().date()
users = []
for delta in range(-2, 8):
    date = today.replace(year=1990) + timedelta(days=delta)
    name = f"Name_{date.month}_{date.day}"
    birthday = date.strftime(date_format)
    users.append({
        "name": name,
        "birthday": birthday
    })
upcoming_birthdays = get_upcoming_birthdays(users)
print("This week's list of greetings:", upcoming_birthdays, "\n")
