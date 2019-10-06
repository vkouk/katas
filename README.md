# Software Craftsmanship Katas in Python

To run these as-is, you'll need to have Python(Latest), Pip & Pytest installed. Then run from the terminal:

```
git clone git@github.com:vkouk/katas.git katas
cd katas
cd rpn
pytest
cd .. && cd weather
pytest
```

## RPN Calculator

An RPN calculator program computes expressions written in Reverse Polish Notation.

The RPN expression: `3 5 8 * 7 + *` equals: `3 * ((5 * 8) + 7)`

Source: https://josepaumard.github.io/katas/introductory/rpncalculator-kata.html

# Data Munging

Part 1: In `bin/weather.dat` you’ll find daily weather data for Morristown, NJ for June 2002. Write a program to output the day number (column one) with the smallest temperature spread (the maximum temperature is the second column, the minimum the third column).

Source: http://codekata.com/kata/kata04-data-munging/
