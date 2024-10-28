def sort_numbers(numbers: str) -> str:
    num_dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
    }
    numbers = [num_dict[num] for num in numbers.split()]
    return ' '.join(str(num) for num in sorted(numbers))

# Code above.

if __name__ == '__main__':
    import doctest
    if doctest.testmod() != 0:
        exit(1)


# Made By Mostafa_Khaled
```
    
```

This code defines a function `sort_numbers` that