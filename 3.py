def flatten_list(my_list):
    result = []
    for element in my_list:
        if type(element) == list:
            result += flatten_list(element)
        else:
            result += [element]
    return result


print(flatten_list([1, [2, [3, [4, 5]]]]))
