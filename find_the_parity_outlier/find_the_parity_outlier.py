def get_type_num(num: int)-> int:
    type_num = 0
    num_is_odd = is_odd(num)

    if num_is_odd:
        type_num = 1

    return type_num

def is_odd(num: int)-> int:

    return num % 2

def get_type_array(arr: list)-> int:
    sum3_indexes = arr[0] + arr[1] + arr[2]
    type_array = get_type_num(sum3_indexes)

    return type_array


# mergesort y binary search...
