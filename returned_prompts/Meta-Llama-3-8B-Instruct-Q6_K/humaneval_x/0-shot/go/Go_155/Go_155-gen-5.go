```go
func EvenOddCount(num int) [2]int {
    even, odd := 0, 0
    for num != 0 {
        digit := num & 1
        if digit == 0 {
            even++
        } else {
            odd++
        }
        num >>= 1
    }
    return [2]int{even, odd}
}
```
The function `EvenOddCount` takes an integer `num` as input and returns a tuple of two integers, where the first integer represents the count of even digits and the second integer represents the count of odd digits.

We use a for loop to iterate over each digit of the input number. We use the bitwise AND operator `&` to get the least significant bit of the number, which represents the current digit. If the digit is 0, we increment the `even` counter, otherwise we increment the `odd` counter.

After processing each digit, we right-shift the number by 1 bit using the bitwise right shift operator `>>=` to move to the next digit.

Finally, we return the tuple `[even, odd]` as the result. The example you provided, `EvenOddCount(-12)`, will return `(1, 1)` because there is one even digit (2) and one odd digit (1). Similarly, `EvenOddCount(123)` will return `(1, 2)` because there is one even digit (1) and two odd digits (3 and 3).