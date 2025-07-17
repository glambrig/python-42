import sys


def encode(s, dict):
    res = str()
    length = 0
    for e in s:
        assert e.isalnum() or e == ' ', ""
        assert dict[e.upper()] in dict.values(), ""
        res += dict[e.upper()]
        if length + 1 != len(s):
            res += ' '
        length += 1
    return res


def main():
    '''
        Make a program that takes a string as an argument
        and encodes it into Morse Code.
    '''

    translation = {
        'A': '.-', 'B': '-...',
        'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-',
        'L': '.-..', 'M': '--', 'N': '-.',
        'O': '---', 'P': '.--.', 'Q': '--.-',
        'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--',
        'X': '-..-', 'Y': '-.--', 'Z': '--..',
        '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....',
        '7': '--...', '8': '---..', '9': '----.',
        '0': '-----', ' ': '/'
    }
    try:
        assert len(sys.argv) == 2, ""
        print(encode(sys.argv[1], translation))
    except AssertionError:
        print("AssertionError: the arguments are bad")
        return


if __name__ == "__main__":
    main()
