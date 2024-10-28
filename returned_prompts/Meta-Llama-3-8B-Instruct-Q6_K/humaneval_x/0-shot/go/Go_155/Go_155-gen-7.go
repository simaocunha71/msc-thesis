
```go
func EvenOddCount(num int) [2]int {
    even, odd := 0, 0
    for num != 0 {
        digit := num % 10
        if digit % 2 == 0 {
            even++
        } else {
            odd++
        }
        num /= 10
    }
    return [2]int{even, odd}
}
```

Explanation:

We use two variables `even` and `odd` to keep track of the count of even and odd digits respectively. We iterate through each digit of the input number using the modulo operator (`%`) to extract the last digit. We then check if the digit is even or odd using another modulo operation (`% 2 == 0` for even and `!= 0` for odd). We increment the corresponding counter (even or odd) and then remove the last digit from the number using integer division (`/=`). Finally, we return a tuple (or array in Go) containing the counts of even and odd digits.

Note: This solution assumes that the input number is non-negative. If you want to handle negative