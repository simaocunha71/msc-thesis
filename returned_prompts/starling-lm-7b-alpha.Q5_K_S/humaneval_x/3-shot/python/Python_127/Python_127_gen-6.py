    # get intersection start and end
    start = max(interval1[0], interval2[0])
    end = min(interval1[1], interval2[1])

    # if intersection start is greater than intersection end, no intersection
    if start > end:
        return "NO"

    # get intersection length
    length = end - start + 1

    # check if length is prime
    is_prime = True
    for i in range(2, length):
        if length % i == 0:
            is_prime = False
            break

    if is_prime:
        return "YES"
    else:
        return "NO"


