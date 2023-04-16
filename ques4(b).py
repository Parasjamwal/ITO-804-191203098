def shift_left(lst):
    """
    Shifts the elements of a list left by one position
    """
    return lst[1:] + [lst[0]]

# example usage
original_list = [1, 2, 3]
shifted_list = shift_left(original_list)
print(shifted_list)
