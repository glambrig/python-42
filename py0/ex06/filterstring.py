import sys
import ft_filter


def main():
    '''
        The program should output a list of words
        from S that have a length greater than N.
    '''

    try:
        args = sys.argv
        assert len(args) == 3, "the arguments are bad"
        assert type(args[1]) is str, "the arguments are bad"
        assert type(int(args[2])) is int, "the arguments are bad"
    except AssertionError as err:
        print(f"AssertionError: {err}")
        return

    num = int(args[2])
    result = ft_filter.ft_filter(lambda s: len(s) > num, args[1].split())
    print(f"{result}")


if __name__ == "__main__":
    main()
