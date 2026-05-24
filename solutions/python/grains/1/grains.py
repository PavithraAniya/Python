def square(number):
    """
    Return the number of grains on square n.
    """

    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    
    return 2 ** (number - 1)


def total():
    
    """
    Return the total number of grains on the chessboard.
    """
    # Sum of geometric series: 2^64 - 1
    return 2 ** 64 - 1

