    for i in range(1,100):
        if a % i == 0:
            count = 0
            for j in range(1, 100):
                if i % j == 0:
                    count += 1
            if count == 2:
                return True
    return False


