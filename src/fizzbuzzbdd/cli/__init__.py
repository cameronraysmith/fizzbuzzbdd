# SPDX-FileCopyrightText: 2023-present Cameron Smith <cameron.ray.smith@gmail.com>
#
# SPDX-License-Identifier: MIT
import click

from fizzbuzzbdd.__about__ import __version__
from fizzbuzzbdd.fizzbuzz import fizzbuzz


@click.command(context_settings={"help_option_names": ["-h", "--help"]})
@click.version_option(version=__version__, prog_name="fizzbuzzbdd")
@click.argument("number", type=click.INT)
def fizzbuzzbdd(number):
    """Play fizzbuzz

    Args:
        number (Int): The number to submit to the FizzBuzz game.
    """
    click.echo(fizzbuzz(number))
