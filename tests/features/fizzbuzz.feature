Feature: FizzBuzz game
  In order to practice TDD
  As a developer
  I want to implement the FizzBuzz game and test it using pytest-bdd

  Scenario: Playing FizzBuzz with a number not divisible by 3 or 5
    Given a number 7
    When I play FizzBuzz
    Then the result should be "7"

  Scenario: Playing FizzBuzz with a number divisible by 3
    Given a number 3
    When I play FizzBuzz
    Then the result should be "Fizz"

  Scenario: Playing FizzBuzz with a number divisible by 5
    Given a number 5
    When I play FizzBuzz
    Then the result should be "Buzz"

  # Scenario: Playing FizzBuzz with a number divisible by both 3 and 5
  #   Given a number 15
  #   When I play FizzBuzz
  #   Then the result should be "FizzBuzz"
