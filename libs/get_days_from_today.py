from datetime import datetime

str_format = "%Y-%m-%d"
human_format = "YYYY-MM-DD"
message_error = f"The value must be a string in the format '{human_format}'"

def get_days_from_today(date: str) -> int:
    try:
        now = datetime.now().date()
        d = datetime.strptime(date, str_format).date()
        result = now - d
        return result.days
    except TypeError:
        print(message_error)
    except ValueError:
        print(message_error)
    return None


if __name__ == "__main__":
    # Test cases
    days = get_days_from_today('2022-02-24')
    print(f"from 2022-02-24: {days} day(s)")

    days = get_days_from_today('2024-12-06')
    print(f"from 2024-12-06: {days} day(s)")

    days = get_days_from_today(datetime.now().strftime(str_format))
    print(f"from today: {days} day(s)")

    # Exceptions
    get_days_from_today("2022-02-24 05:00:00")
    get_days_from_today("-2020-02-20")
    get_days_from_today("202-02-20")
    get_days_from_today(1)
    get_days_from_today(None)
    get_days_from_today("")
    get_days_from_today({})
