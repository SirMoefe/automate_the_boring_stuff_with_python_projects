"""Comma Code"""

spam = ["apples", "bananas", "tofu", "cats"]
ham = ["pig"]
bacon = []


def join_list(list):
    if len(list) < 1:
        return "The list is empty. Add some values!"
    elif len(list) < 2 and len(list) > 0:
        for value in list:
            return value
    else:
        counter = 0
        join = ""
        while counter < len(list) - 1:
            join += list[counter] + ", "
            counter += 1
        join += "and " + list[-1]
        return join


print(join_list(ham))
