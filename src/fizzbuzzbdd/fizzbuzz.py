from beartype import beartype


@beartype
def fizzbuzz(number: int) -> str:
    """Execute one round of the FizzBuzz game.

    Args:
        number (Int): The number to submit to the FizzBuzz game.

    Returns:
        str: The result of the FizzBuzz game.
    """
    divisible_by_three = number % 3 == 0
    divisible_by_five = number % 5 == 0

    if divisible_by_three and divisible_by_five:
        result = "FizzBuzz"
    elif divisible_by_three:
        result = "Fizz"
    elif divisible_by_five:
        result = "Buzz"
    else:
        result = str(number)

    return result
