def all_thing_is_obj(object: any) -> int:
    match str(type(object)):
        case "<class 'list'>":
            print(f"List : {type(object)}")
        case "<class 'tuple'>":
            print(f"Tuple : {type(object)}")
        case "<class 'set'>":
            print(f"Set : {type(object)}")
        case "<class 'dict'>":
            print(f"Dict : {type(object)}")
        case "<class 'str'>":
            print(f"{object} is in the Kitchen : {type(object)}")
        case _:
            print("Type not found")
    return 42
