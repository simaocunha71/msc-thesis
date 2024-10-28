You can solve this problem by iterating through each digit of the number and checking if it's even or odd, then incrementing the corresponding counter. Here's an example implementation:

```go
func EvenOddCount(num int) [2]int {
    if num < 0 {
        num = -num
    }
    count := [2]int{0, 0}
    for num > 0 {
        digit := num % 10
        if digit%2 == 0 {
            count[0]++
        } else {
            count[1]++
        }
        num /= 10
    }
    return count
}
```

In this implementation, we first check if the number is negative and make it positive if it is. Then we initialize a count array with two elements, where the first element represents the count of even digits and the second element represents the count of odd digits. 

We then iterate through each digit of the number by using the modulo operator (%). If the digit is even (i.e., divisible by 2), we increment the count of even digits. Otherwise, we increment the count of odd digits. 

Finally, we return the count array.

This solution has a time complexity of O(log10(num)), where num is the input number.