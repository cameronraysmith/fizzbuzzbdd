from pytest_bdd import given, scenarios, then, when
from pytest_bdd.parsers import cfparse

from fizzbuzzbdd.fizzbuzz import fizzbuzz

scenarios("../features/fizzbuzz.feature")


@given(cfparse("a number {number:Number}", extra_types={"Number": int}), target_fixture="game_input")
def game_input(number):
    return number


@when(cfparse("I play FizzBuzz"))
def play_fizzbuzz(game_input):
    return fizzbuzz(game_input)


@then(cfparse('the result should be "{output}"'))
def fizzbuzz_result(game_input, output):
    assert play_fizzbuzz(game_input) == output
