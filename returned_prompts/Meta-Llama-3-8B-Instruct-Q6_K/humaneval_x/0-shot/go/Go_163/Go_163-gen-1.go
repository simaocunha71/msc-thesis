```
    if a > b {
        a, b = b, a
    }
    result := make([]int, 0)
    for i := a; i <= b; i++ {
        str := strconv.Itoa(i)
        for j := 0; j < len(str); j++ {
            digit := int(str[j] - '0')
            if digit%2 == 0 {
                result = append(result, i)
                break
            }
        }
    }
    return result
}
```


Solution:

The problem is asking for a function that takes two positive integers `a` and `b` and returns a slice of integers that are even digits between `a` and `b`, in ascending order.

Here is a solution in Go:
```
func GenerateIntegers(a, b int) []int {
    if a > b {
        a, b = b, a
    }
    result := make([]int, 0)
    for i := a; i <= b; i++ {
        str := strconv.Itoa(i)
        for j := 0; j < len(str); j++ {
            digit := int(str[j] - '0')
            if digit%2 == 0 {
                result = append(result, i)
                break
            }
        }
    }
    return result
}
```
This function first checks if `a` is greater than `b` and swaps them if necessary. Then it iterates over the range of numbers from `a` to `b` (inclusive). For each number, it converts it to a string and iterates over each character (digit) in the string. If the digit is even (i.e., `digit % 2 == 0`), it appends the current number to the result slice and breaks out of the inner loop. Finally, it returns the result slice.

Note that this function returns a slice of integers that are even digits between `a` and `b`, but not necessarily the smallest even digits. For example, if `a` is 10 and `b` is 14, the function will return `[10, 12, 14]`, not `[10, 12]`. If you want to get the smallest even digits, you can modify the function to keep track of the smallest even digit seen so far and return it if it's less than or equal to the current digit. Here is an updated version of the function:
```
func GenerateIntegers(a