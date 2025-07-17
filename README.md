Since I forgot to bring a notebook, here's all the python stuff I've learned so far.

-------------------------------------------------

### Things that hold stuff (like C structs):
    List:
        my_list = [1, 2, 3]
        Ordered, changeable, allows dup values
    Tuple:
        my_tuple = (1, 2, 3)
        Ordered, unchangeable, allows dup values
    Set:
        my_set = {"apple", "banana", "cherry"}
        Unordered, unchangeable*, forbids dup values

        *items are unchangeable, but you can remove and add new items in the set.
    Dictionnary:
        my_dict = {"name": "bob", "age": 99}
        Ordered (since python 3.7), changeable, forbids dup values

    "Ordered": Items have a defined order, order doesn't change, new items placed at end of container.
    "Changeable": Items in container can be added, modified, or removed.
    "Unordered": Items can appear in a different order every time you use them, and cannot be referred to by index or key.
    "Allows dup values": Containers with indices can have items with the same value.

    An empty list/tuple/set/dict can be created using either:
        1. Its respective operator ([] for list, etc.)
        2. The list(), tuple(), etc. constructor

    To check whether an element is found in a list/tuple/set/dict, use the 'in' keyword:
        if {elem} in {container}:
            {...}

### Working with time/date:
    Two modules: 'time' and 'datetime'
        time.time() -> seconds since epoch
        datetime.datetime.now() -> current date and time

        datetime has a bunch of methods to format the returned object (see strftime())

### Python types:
    list of types: https://www.w3schools.com/python/python_datatypes.asp
    str methods: https://www.w3schools.com/python/python_strings_methods.asp
    
    type(object) -> type of thing passed as param

### Null types:
    Technically there are lots of ways to say that something is (or contains) nothing.

    'None' is the only instance of the class 'NoneType'. Functions that don't return anything implicitely return 'None'. It's also used as a "nothing found" return value,
        e.g. a search method that didn't find anything, -> None
    
    There's also 'False', '0', '' (empty string), NaN (for floats).

### Handling command line arguments:
    Module: 'sys'
        sys.argv is a list (type == list) with arguments inside

### Assertions:
    Assertions are a tool to make sure that something is the case before running the next line of code. Triggering the assert statement will throw an exception of type AssertionError.
    Syntax: assert {condition}, {error message}

    e.g. assert type(bob) is person, "bob's not human, something is wrong"
        ---> "Make sure 'bob' is of type 'person'. If that's not the case, throw an AssertionError with the message "bob's not human, something is wrong""

    Note that unlike if/else statements, assert throws the exception when the condition is NOT true.
        ---> if 123 > 0: {...} -> Runs the block of code
        ---> assert 123 > 0, "..." -> Jumps to the next line, does NOT throw an exception, since 123 is greater than 0.

### Exception handling:
    Pretty much like in C/C++, with a couple extra keywords: try, except, else, finally.

    You can have multiple except statements to catch different exception types:
    try:
        {...}
    except AssertionError as err:
        print("Caught AssertionError")
    except:
        print("Caught something else")


    'else' runs code when nothing went wrong
    try:
        {...}
    except:
        print("Caught something")
    else:
        print("All good.")
        {...}


    'finally' always runs, regardless of whether an exception occurred or not.
    try:
        {...}
    except:
        print("Caught something")
    else:
        print("All good.")
        {...}
    finally:
        print("This always runs")

### Lambda functions:
    These are nameless functions. The result of the expression is returned as the result of the lambda function.
    Syntax: lambda {parameters} : {expression}

    Example:
        numberTimesFive = lambda num : num * 5

### List comprehension:
    This is a shorter way of defining how a new list should be built from an old one. You could do this with a loop, but list comprehension makes it shorter and easier.
    Syntax: newlist = [{expression} for {item} in {iterable} if {condition} == True]
        (The condition is optional and can be omitted)
    The {expression} at the beginning of the list comprehension statement is the element that will be added to the new list if the condition is true.

### The 'yield' keyword:
    Returns a list of multiple values, one for each 'yield' statement. Unlike 'return', execution continues after a 'yield' statement.
    Syntax: yield {value}

    Example:
        def f():
            yield "hello"
            yield "world"
            yield '!'
            {...}
        result = f()
        #result will be ["hello", "world", '!']

-------------------------------------------------
## Miscellaneous useful functions:

### The filter() function:
    Syntax: filter({function}, {iterable})
        'iterable' == list/tuple/set/dict
    Returns an object of the same type as the iterable, but with stuff filtered out by the function.

    Example:
        def f(arg):
            if (type(arg) == str)
                return true
            else
                return False
            
        list = ['a', 123, "hello"]
        new_list = filter(f, list)
        
        #new_list would be ['a', "hello"]
