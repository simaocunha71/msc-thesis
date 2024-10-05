    eaten = number + need - remaining
    left = remaining - (number + need - remaining)
    return [eaten, left] if eaten >= 0 else [eaten + remaining, 0]  # if eaten is negative then we will eat remaining carrots and return total eaten as remaining and 0 as left

    # if there are not enough remaining carrots, we will eat all remaining carrots, but will still be hungry.
    # so we return the total number of eaten carrots and the number of carrots left which is 0.