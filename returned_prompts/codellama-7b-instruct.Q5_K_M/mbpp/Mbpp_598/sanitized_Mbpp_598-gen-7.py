def armstrong_number(n):
    """
    :param n: integer
    :return: boolean
    """
    # calculate the cube of the number
    n_cube = n ** 3
    # extract the integer part
    n_cube = int(n_cube)
    # check whether the cube is equal to the number
    return n_cube == n