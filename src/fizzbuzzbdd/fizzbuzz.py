from beartype import beartype


@beartype
def fizzbuzz(number: int) -> str:  # sourcery skip: lift-return-into-if
    """Execute one round of the FizzBuzz game.

    Args:
        number (Int): The number to submit to the FizzBuzz game.

    Returns:
        str: The result of the FizzBuzz game.

    Example:
        >>> from fizzbuzzbdd.fizzbuzz import fizzbuzz
        >>> assert(fizzbuzz(3) == "Fizz")
        >>> assert(fizzbuzz(5) == "Buzz")
        >>> assert(fizzbuzz(15) == "FizzBuzz")
        >>> assert(fizzbuzz(7) == "7")
        >>> assert(fizzbuzz(1010107) == "1010107")
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
