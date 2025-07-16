def ft_filter(func, iterable):
    '''replaces real filter() function'''

    # print(f"{type(iterable)}")

    newContainer = None

    match type(iterable):
        case "list":
            newContainer = list()
        case "tuple":
            newContainer = tuple()
        case "set":
            newContainer = set()
        case "dict":
            newContainer = dict()

    for e in iterable:
        if func(e):
            newContainer.append(e)
    return newContainer
