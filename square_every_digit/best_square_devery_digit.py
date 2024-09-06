def square_digits(num):
    result = 0
    multiplier = 1
    while num:
        digit = num % 10
        result += digit ** 2 * multiplier
        multiplier *= (10, 100)[digit > 3]
        num //= 10
                                        
    return result

print(square_digits(12345))