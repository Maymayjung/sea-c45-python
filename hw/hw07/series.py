def fibonacci(n):

    if (n == 0):
        return 0

    elif (n == 1):
        return 1

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):

    """Return the nth number from the Lucas sequence.

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
