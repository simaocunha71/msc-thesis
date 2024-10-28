    result = []
    for i in range(len(numbers)-1):
        result.append(numbers[i])
        result.append(delimeter)
    result.append(numbers[len(numbers)-1])
    return result


def intersperse_2(numbers: List[int], delimeter: int) -> List[int]:
    return [numbers[i] for i in range(len(numbers))] + [delimeter]


def intersperse_3(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i in range(len(numbers)-1):
        result.append(numbers[i])
        result.append(delimeter)
    result.append(numbers[len(numbers)-1])
    return result


def intersperse_4(numbers: List[int], delimeter: int) -> List[int]:
    return numbers + [delimeter] * (len(numbers)-1)


def intersperse_5(numbers: List[int], delimeter: int) -> List[int]:
    return [numbers[i] for i in range(len(numbers))] + [delimeter] * (len(numbers)-1)


if __name__ == "__main__":
    print(intersperse([1, 2, 3], 4))
    print(intersperse_2([1, 2, 3], 4))
    print(intersperse_3([1, 2, 3], 4))
    print(intersperse_4([1, 2, 3], 4))
    print(intersperse_5([1, 2, 3], 4))




#  通过对比，我们可以看出，第二种方法是最简洁的，但是它也有一个缺点，即它需要在每次运行中创建一个新的列表，因此在某些情况下，它可能不是最高效的。
#  第三种方法和第四种方