import sys

args = sys.argv

# print(len(args))

try:
    assert len(args) <= 2, "more than one argument provided"
    assert type(int(args[1])) is int, "argument is not an integer"
    if int(args[1]) % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
except AssertionError as err:
    print(f"AssertionError: {err}")
except:
    _ = 123 #do nothing