def fibonacci(n):

    """The Fibonacci numbers are the integer sequence \
    0, 1, 1, 2, 3, 5, 8, 13, 21, ..., in which each item is formed by \
    adding the previous two.
    The Fibonacci sequence up to n-th term using recursive functions.

    Example:
        def fib(n):
            if n==1 or n==2:
            return 1
            return fib(n-1)+fib(n-2)
        print fib(5)

    """
    if (n == 0):
        return 0

    elif (n == 1):
        return 1

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):

    """The sequence of Lucas numbers is: 2,1,3,4,7,11,18,29,47,76,123...
    Return the nth number from the Lucas sequence.
    Example:
    lucas(0) = 2
    lucas(1) = 1
    ...
    lucas(n - 1) + lucas(n - 2)
    """

    if (n == 0):
        return 2
    elif (n == 1):
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)


def sum_series(n, zeroth=0, oneth=1):

    """Example:
    sum_series(0) == zeroth
    sum_series(1) == oneth
    ...
    sum_series(n) == sum_series(n - 1) + sum_series(n - 2)
    """

    if (n == 0):
        return zeroth
    elif (n == 1):
        return oneth
    else:
        return sum_series(n - 1, zeroth, oneth) + \
            sum_series(n - 2, zeroth, oneth)
