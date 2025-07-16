import sys
import ft_filter

def find_larger_than_n(str):
    res = lambda num, str : len(str) > num
    return res

def main():
    '''
        The program should output a list of words
        from S that have a length greater than N.
    '''

    try:
        args = sys.argv
        assert args == 3, "the arguments are bad"
        assert type(args[1]) == "<class 'str'>", "the arguments are bad"
        assert type(int(args[2])) == "<class 'int'>", "the arguments are bad"
    except AssertionError as err:
        print(f"AssertionError: {err}")

    global num
    num = int(args[2])
    result = ft_filter.ft_filter(find_larger_than_n, args[1])
    print(f"{result}")

if __name__ == "__main__":
    main()
