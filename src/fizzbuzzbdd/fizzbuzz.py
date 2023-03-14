from beartype import beartype


@beartype
def fizzbuzz(number: int) -> str:
    """Execute one round of the FizzBuzz game.

    Args:
        number (Int): The number to submit to the FizzBuzz game.

    Returns:
        str: The result of the FizzBuzz game.
    """
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return str(number)
