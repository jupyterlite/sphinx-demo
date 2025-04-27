"""Even though the docstrings in the function below contain Examples sections in
the NumPy style format, no TryExamples buttons will be displayed, as this page is
included in the ignore_patterns list in try_examples.json.
"""

def square_number(x):
    """Return the square of a number.

    Parameters
    ----------
    x : number
        The number to square.

    Returns
    -------
    number
        The square of the input number.

    Examples
    --------
    Square some numbers:

    >>> square_number(4)
    16
    >>> square_number(2.5)
    6.25

    Use with a list comprehension:

    >>> numbers = [1, 2, 3, 4, 5]
    >>> squares = [square_number(n) for n in numbers]
    >>> print(squares)
    [1, 4, 9, 16, 25]
    """
    return x * x
