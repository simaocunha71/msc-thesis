    l.sort()
    for i in range(len(l) - 2):
        left = i + 1
        right = len(l) - 1
        while left < right:
            s = l[i] + l[left] + l[right]
            if s < 0:
                left += 1
            elif s > 0:
                right -= 1
            else:
                return True
    return False


