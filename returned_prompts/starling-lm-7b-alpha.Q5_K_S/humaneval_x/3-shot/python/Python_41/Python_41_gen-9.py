    # The problem is asking about collisions between the two sets of cars. The cars in the first set
    # are all moving left to right, and the cars in the second set are moving right to left.  The cars
    # in the second set are all the same speed and same trajectory, but mirrored.  As a result,
    # the collision of car i moving left to right and car j moving right to left is equivalent to
    # car j moving left to right and car i moving right to left.  As a result, we can simply count
    # the number of collisions in the left-to-right set and return that count.
    return n * (n - 1) // 2


