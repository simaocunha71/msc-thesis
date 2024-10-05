
    def unique_digits(x):
        result = []
        for num in x:
            if all(int(digit) % 2 != 0 for digit in str(num)):
                result.append(num)
        return sorted(result)

    print(unique_digits([15, 33, 1422, 1]))
    print(unique_digits([152, 323, 1422, 10]))

