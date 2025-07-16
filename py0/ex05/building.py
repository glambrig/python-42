import sys


def display_sum():
    '''
        takes a single string argument and displays the sums
        of its upper-case characters, lower-case
        characters, punctuation characters, digits and spaces.
    '''
    args = sys.argv

    try:
        assert len(args) == 2, "Too many or no arguments provided"

        punctuation = ['.', ',', '\'', '\"', '-', '?', '!', ';', ':']
        spaces = [' ', '\r']
        upperCount = 0
        lowerCount = 0
        punctCount = 0
        spaceCount = 0
        digitCount = 0

        for e in args[1]:
            if e.isascii() and e.isprintable():
                if e.isupper():
                    upperCount = upperCount + 1
                    continue
                elif e.islower():
                    lowerCount = lowerCount + 1
                    continue
                elif e.isdigit():
                    digitCount = digitCount + 1
                    continue
                elif e in spaces:
                    spaceCount = spaceCount + 1
                    continue
                elif e in punctuation:
                    punctCount = punctCount + 1

        totalCount = upperCount + lowerCount + punctCount
        + spaceCount + digitCount
        print(f"The text contains {totalCount} characters:")
        print(f"{upperCount} upper characters")
        print(f"{lowerCount} lower characters")
        print(f"{punctCount} punctuation marks")
        print(f"{spaceCount} spaces")
        print(f"{digitCount} digits")

    except AssertionError as err:
        print(f"AssertionError: {err}")


def main():
    display_sum()


if __name__ == "__main__":
    main()
