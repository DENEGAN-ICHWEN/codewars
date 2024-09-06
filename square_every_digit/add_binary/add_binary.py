def add_binary(a,b)-> str:
    """
    Function that adds two integers and converts the result into
    its binary representation.

    Args:
        a (int): Any integer.
        b (int): Any integer.

    Returns:
        str: the sum's binary representation.
    """
    sum = a + b
    binary = bin(sum)[2:]

    return binary

print(add_binary(0, 0))