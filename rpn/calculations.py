import math


def plus_numbers(arr):
    return arr.pop() + arr.pop()


def minus_numbers(arr):
    prevNum = arr.pop()
    return arr.pop() - prevNum


def multiple_numbers(arr):
    return arr.pop() * arr.pop()


def divide_numbers(arr):
    prevNum = arr.pop()
    return arr.pop() / prevNum


def sqrt_numbers(arr):
    return math.sqrt(arr.pop())


def max_numbers(arr):
    return max(arr)
