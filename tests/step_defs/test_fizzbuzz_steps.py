import pytest
from pytest_bdd import given, scenarios, then, when

from fizzbuzzbdd.fizzbuzz import fizzbuzz

scenarios("../features/fizzbuzz.feature")


# @pytest.fixture
@given("a number 7", target_fixture="number")
def number():
    return 7


@when("I play FizzBuzz")
def play_fizzbuzz(number):
    return fizzbuzz(number)


@pytest.fixture
def result(number):
    return str(number)


@then('the result should be "7"')
def fizzbuzz_result(number, result):
    assert play_fizzbuzz(number) == result
