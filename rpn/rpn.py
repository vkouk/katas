import calculations

operators = {
    '+': calculations.plus_numbers,
    '-': calculations.minus_numbers,
    '*': calculations.multiple_numbers,
    '/': calculations.divide_numbers,
    'SQRT': calculations.sqrt_numbers,
    'MAX': calculations.max_numbers
}


def splitStr(input):
    if type(input) is not str:
        raise Exception('Invalid argument for str field')
    return input.split(' ')


def rpn_calculation(input):
    if type(input) is not str:
        raise Exception('Invalid argument for input field')
    arr = splitStr(input)
    output = []
    for entry in arr:
        if entry in operators:
            output.append(operators[entry](output))
        else:
            output.append(int(entry))
    return output[0]
