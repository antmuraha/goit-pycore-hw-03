import random

MIN = 1
MAX = 1000


def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    for val in [min, max, quantity]:
        if not isinstance(val, int):
            return []

    if max > MAX or max < min + 1:
        return []
    if min < MIN or min >= max:
        return []
    if quantity < 0 or quantity > max - min:
        return []

    result = random.sample(range(min, max), k=quantity)
    return sorted(result)


if __name__ == "__main__":
    # Test cases
    lottery_numbers = get_numbers_ticket(1, 99, 5)
    print("Your lottery numbers:", lottery_numbers)

    lottery_numbers = get_numbers_ticket(5, 6, 1)
    print("Your lottery numbers:", lottery_numbers)

    lottery_numbers = get_numbers_ticket(1, 1000, 1)
    print("Your lottery numbers:", lottery_numbers)

    # Exceptions
    args = [
        [0, 100, 5],
        [1, 1001, 5],
        [2, 100, 99],
        ["1", 9, 49],
        [1, 9, None],
    ]
    for vals in args:
        result = get_numbers_ticket(*vals)
        if len(result) == 0:
            print(f"The entered values {vals} are incorrect")
