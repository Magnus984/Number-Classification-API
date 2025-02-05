def is_prime(n: int) -> bool:
    """
    Check if a number is prime.

    :param n: The number to check.
    :return: True if the number is prime, False otherwise.
    """
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True