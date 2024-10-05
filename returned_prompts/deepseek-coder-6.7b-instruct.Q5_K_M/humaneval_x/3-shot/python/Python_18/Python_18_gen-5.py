    count = 0
    position = 0
    while True:
        position = string.find(substring, position)
        if position == -1:
            return count
        count += 1
        position += 1


