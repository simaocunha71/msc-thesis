    l.sort()

    for i in range(len(l) - 2):
        left = i + 1
        right = len(l) - 1

        while left < right:
            current_sum = l[i] + l[left] + l[right]

            if current_sum == 0:
                return True

            if current_sum > 0:
                right -= 1
            else:
                left += 1

    return False

