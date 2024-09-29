import random

MIN = 1
MAX = 1000

ARG_MIN = "min"
ARG_MAX = "max"
ARG_QUANTITY = "quantity"


def get_numbers_ticket_with_exceptions(min: int, max: int, quantity: int) -> list:
    for val in [min, max, quantity]:
        if not isinstance(val, int):
            raise ExceptionValueType()

    if max > MAX or max < min + 1:
        raise ExceptionValueRange(ARG_MAX)
    if min < MIN or min >= max:
        raise ExceptionValueRange(ARG_MIN)
    if quantity < 0 or quantity > max - min:
        raise ExceptionValueRange(ARG_QUANTITY)

    result = random.sample(range(min, max), k=quantity)
    return sorted(result)


class ExceptionValueType(Exception):
    def __init__(self, message="Input values min, max, quantity must be integers"):
        super().__init__(message)


class ExceptionValueRange(Exception):
    messages = {
        ARG_MIN: f"The minimum value must be greater than {MIN - 1} and less than 'max'",
        ARG_MAX: f"The maximum value must be greater than 'min' and less or equal than {MAX}",
        ARG_QUANTITY: f"The quantity value must be greater than 0 and less or equal than (max - min)"
    }

    def __init__(self, arg_name: str):
        super().__init__(ExceptionValueRange.messages[arg_name])


if __name__ == "__main__":
    # Test cases
    lottery_numbers = get_numbers_ticket_with_exceptions(1, 99, 5)
    print("Your lottery numbers:", lottery_numbers)

    lottery_numbers = get_numbers_ticket_with_exceptions(5, 6, 1)
    print("Your lottery numbers:", lottery_numbers)

    lottery_numbers = get_numbers_ticket_with_exceptions(1, 1000, 1)
    print("Your lottery numbers:", lottery_numbers)

    # Exceptions
    args = [
        [0, 100, 5],
        [1, 1001, 5],
        [1, 2, 2],
        ["1", 9, 49],
        [1, 9, None],
    ]
    for vals in args:
        try:
            get_numbers_ticket_with_exceptions(*vals)
        except ExceptionValueType as e:
            print(f"Error: {e}. Input: {vals}")
        except ExceptionValueRange as e:
            print(f"Error: {e}. Input: {vals}")
