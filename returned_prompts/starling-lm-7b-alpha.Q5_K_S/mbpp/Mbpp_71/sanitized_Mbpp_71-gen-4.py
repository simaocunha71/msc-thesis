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