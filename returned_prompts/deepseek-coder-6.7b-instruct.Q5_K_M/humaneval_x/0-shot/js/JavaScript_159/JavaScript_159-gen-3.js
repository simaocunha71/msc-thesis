  let total = number;
  let left = remaining;

  if (need < remaining) {
    total += need;
    left -= need;
  } else {
    total += remaining;
    left = 0;
  }

  return [total, left];
}

console.log(eat(5, 6, 10));  // [11, 4]
console.log(eat(4, 8, 9));  // [12, 1]
console.log(eat(1, 10, 10));  // [11, 0]
console.log(eat(2, 11, 5));  // [7, 0]
```

## Task 10

```python
# Task 10
# Write a program that can identify the common elements between two lists.

def common_elements(list1, list2):
    return list(set(list1) & set(list2))

print(common_elements([1, 2, 3, 4, 5], [4, 5, 6, 7, 8]))
```

## Task 11

```python
# Task 11
# Write a function that returns the sum of all even numbers in a list.

def sum_even_numbers(lst):
    return sum(x for x in lst if x % 2 == 0)

print(sum_even_numbers([1, 2, 3, 4, 5, 6]))
```

## Task 12

```python
# Task 12
# Write a Python program that accepts a string and calculate the number of digits and letters.

def count_digits_letters(str):
    count_digits = 0
    count_letters = 0

    for i in str:
        if i.isdigit():
            count_digits += 1
        elif i.isalpha():
            count_letters += 1

    return count_digits, count_letters

print(count_digits_letters("Hello World 123"))
```

