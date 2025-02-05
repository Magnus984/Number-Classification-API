def is_perfect(n: int) -> bool:
    """
    Check if a number is perfect.

    :param n: The number to check.
    :return: True if the number is perfect, False otherwise.
    """
    n = abs(n)
    if n < 2:
        return False

    divisors = [1]
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n // i)

    return sum(divisors) == n