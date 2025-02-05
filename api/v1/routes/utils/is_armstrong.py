def is_armstrong(number):
    """
    Check if a number is an Armstrong number.

    :param number: The number to check.
    :return: True if the number is an Armstrong number, False otherwise.
    """
    number = str(abs(number))
    n = len(number)
    return sum(int(digit) ** n for digit in number) == int(number)