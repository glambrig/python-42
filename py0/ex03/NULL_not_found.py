def NULL_not_found(object: any) -> int:
    match str(type(object)):
        case str("<class 'NoneType'>"):
            print(f"Nothing: {object} {type(object)}")
            return 0
        case str("<class 'float'>"):
            print(f"Cheese: {object} {type(object)}")
            return 0
        case str("<class 'int'>"):
            print(f"Zero: {object} {type(object)}")
            return 0
        case str("<class 'str'>"):
            if len(object) == 0:
                print(f"Empty: {type(object)}")
                return 0
            else:
                print("Type not found")
                return 1
        case str("<class 'bool'>"):
            print(f"Fake: {object} {type(object)}")
            return 0
        case _:
            print("Type not found")
    return 1
