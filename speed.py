#! /usr/bin/env python
"""
Timings for 3 types of Python print format statements
Code from F-strings In Python: Everything You Need To Know 
  at https://youtu.be/Mfmr_Puhtew 
"""

import timeit
from string import Template

def perc_format():
    name = "Pat Kelly"
    country = "Texas"
    _ = "%s is from %s." % (name, country)

def str_format():
    name = "Pat Kelly"
    country = "Texas"
    _ = "{} is from {}.".format(name, country)

def f_string():
    name = "Pat Kelly"
    country = "Texas"
    _ = f"{name} is from {country}."

TEMPLATE = Template("$name is from $country.")

def template():
    name = "Pat Kelly"
    country = "Texas"
    _ = TEMPLATE.substitute(name=name, country=country)

def main() -> None:
    print(
        "perc_format:",
        time.timeit(
            perc_format,
            number=100000,
        )
    )

    print(
        "str_format:",
        time.timeit(
            str_format,
            number=100000,
        )
    )

    print(
        "f_string:",
        time.timeit(
            f_string,
            number=100000,
        )
    )
