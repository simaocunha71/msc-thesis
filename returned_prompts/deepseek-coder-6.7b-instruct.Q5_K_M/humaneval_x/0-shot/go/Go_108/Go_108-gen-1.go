
    var count int
    for _, num := range arr {
        sum := 0
        str := strconv.Itoa(num)
        for _, ch := range str {
            digit, _ := strconv.Atoi(string(ch))
            sum += digit
        }
        if sum > 0 {
            count++
        }
    }

    return count
}

```

## Pseudo code

```
function CountNums(arr):
    count = 0
    for each num in arr:
        sum = 0
        str = convert num to string
        for each ch in str:
            digit = convert ch to integer
            sum += digit
        if sum > 0:
            count += 1
    return count
```

## Explanation

This function iterates over each number in the array and calculates the sum of its digits. If this sum is greater than 0, it increments the count. Finally, it returns the count.

## Time complexity

The time complexity of this function is O(n*m), where n is the number of elements in the array and m is the average number of digits in the numbers. This is because it iterates over each number in the array and then over each digit in the number.

## Space complexity

The space complexity of this function is O(n), where n is the number of elements in the array. This is because it stores the count of the numbers with a sum of digits greater than 0.

## Test cases

```
print(CountNums([]) == 0)
print(CountNums([-1, 11, -11]) == 1)
print(CountNums([1, 1, 2]) == 3)
```

## Python code

```python
def CountNums(arr):
    count = 0
    for num in arr:
        sum = 0
        str_num = str(num)
        for ch in str_num:
            digit = int(ch)
            sum += digit
        if sum > 0:
            count += 1
    return count
```

## Test cases

```python
print(CountNums([]) == 0)
