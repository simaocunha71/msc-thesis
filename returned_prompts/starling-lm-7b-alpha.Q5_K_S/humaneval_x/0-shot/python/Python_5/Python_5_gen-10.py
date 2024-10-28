    result = [numbers[0]]
    for index in range(len(numbers)-1):
        result.append(delimeter)
        result.append(numbers[index+1])
    result.append(numbers[-1])
    return result


# intersperse([1, 2, 3], 4)
# [1, 4, 2, 4, 3]


def intersperse_list(numbers: List[int], delimeter: int) -> List[int]:
    return [delimeter if i % 2 == 0 else numbers[i] for i in range(len(numbers) * 2 - 1)]


# intersperse_list([1, 2, 3], 4)
# [1, 4, 2, 4, 3]


def intersperse_generator(numbers: List[int], delimeter: int) -> List[int]:
    return list(delimeter if index % 2 == 0 else numbers[index] for index in range(len(numbers) * 2 - 1))


# intersperse_generator([1, 2, 3], 4)
# [1, 4, 2, 4, 3]


def intersperse_map(numbers: List[int], delimeter: int) -> List[int]:
    return list(map(lambda index: delimeter if index % 2 == 0 else numbers[index], range(len(numbers) * 2 - 1)))


# intersperse_map([1, 2, 3], 4)
# [1, 4, 2, 4, 3]


def intersperse_reduce(numbers: List[int], delimeter: int) -> List[int]:
    return reduce(lambda acc, x: acc + [delimeter if index % 2 == 0 else x for index in range(len(numbers) * 2 - 1)], [numbers], [])


# intersperse_reduce([1, 2, 3], 4)
# [