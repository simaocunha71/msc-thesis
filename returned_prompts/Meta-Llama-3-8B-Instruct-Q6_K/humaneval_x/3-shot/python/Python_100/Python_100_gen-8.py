    result = []
    n_stones = n
    while n_stones > 0:
        if n_stones % 2 == 0:
            result.append(n_stones)
            n_stones -= 1
        else:
            result.append(n_stones)
            n_stones -= 2
    return result[::-1]  # Reverse the list


