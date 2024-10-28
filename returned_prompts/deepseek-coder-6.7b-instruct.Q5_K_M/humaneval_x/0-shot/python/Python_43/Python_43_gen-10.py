
    l.sort()
    left = 0
    right = len(l) - 1

    while left < right:
        sum = l[left] + l[right]

        if sum < 0:
            left += 1
        elif sum > 0:
            right -= 1
        else:
            return True

    return False


if __name__ == "__main__":
    import doctest

    doctest.testmod()


