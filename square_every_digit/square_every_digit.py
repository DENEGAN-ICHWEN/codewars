def square_digits(num)-> int:
    """
    Function that squares every digit of a number and concatenates them.

    Args:
        num (int): Any number.

    Returns:
        int: An integer that has concatenated all the squared digits of the original number.
    """
    array_digits = split_num_into_digits(num)
    result = ""

    for digit in array_digits:
        squared_digit = digit ** 2
        squared_digit_str = int_to_str(squared_digit)
        result += squared_digit_str

    result = str_to_int(result)

    return result

def int_to_str(num)-> str:
    """
    A function that encapsulates the conversion of an integer to a string.
    Note: I made this simple function for good practices (scalability) and encapsulation.

    Args:
        num (int): Any number.

    Returns:
        str: The string of the integer.
    """

    return str(num)

def str_to_int(string)-> int:
    """
    A function that encapsulates the conversion of a string to an integer.
    Note: I made this simple function for good practices (scalability) and encapsulation.

    Args:
        string (str): Any string.

    Returns:
        int: The string converted to an integer.
    """

    return int(string)

def split_num_into_digits(num)-> list:
    """
    Function that splits an integer into the digits that compose it.

    Args:
        num (int): Any integer.

    Returns:
        list: A list with all the digits of the original integer.
    """
    string_num = int_to_str(num)
    array_digits = []

    for digit in string_num:
        digit_int = str_to_int(digit)
        array_digits.append(digit_int)

    return array_digits

print(square_digits(12345))
