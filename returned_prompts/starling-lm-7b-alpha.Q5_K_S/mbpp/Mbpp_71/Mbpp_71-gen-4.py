"""
def comb_sort(numbers):
    numbers_len = len(numbers)
    gap = numbers_len
    swapped = True

    while gap != 0 and swapped:
        gap = gap / 1.3
        swapped = False
        for i in range(numbers_len - gap):
            if numbers[i] > numbers[i + gap]:
                temp = numbers[i]
                numbers[i] = numbers[i + gap]
                numbers[i + gap] = temp
                swapped = True
    return numbers

def test_comb_sort():
    assert comb_sort([5, 15, 37, 25, 79]) == [5, 15, 25, 37, 79]
    print("All tests passed!")

if __name__ == "__main__":
    test_comb_sort()
"""

def comb_sort(numbers):
    numbers_len = len(numbers)
    gap = numbers_len
    swapped = True
    while gap != 0 and swapped:
        gap = gap / 1.3
        swapped = False
        for i in range(numbers_len - gap):
            if numbers[i] > numbers[i + gap]:
                temp = numbers[i]
                numbers[i] = numbers[i + gap]
                numbers[i + gap] = temp
                swapped = True
    return numbers

def test_comb_sort():
    assert comb_sort([5, 15, 37, 25, 79]) == [5, 15, 25, 37, 79]
    print("All tests passed!")

if __name__ == "__main__":
    test_comb_sort()









"""
def comb_sort(numbers):
    numbers_len = len(numbers)
    gap = numbers_len
    swapped = True
    while gap != 0 and swapped:
        gap = gap / 1.3
        swapped = False
        for i in range