```go
func EvenOddCount(num int) [2]int {
    var even, odd int
    for num != 0 {
        digit := num % 10
        if digit%2 == 0 {
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
The problem is asking to write a function that takes an integer as input and returns a tuple containing the count of even and odd digits in the integer.

We can solve this problem by using a for loop to iterate through each digit of the integer. We can use the modulo operator (`%`) to get the last digit of the integer, and then check if the digit is even or odd by using another modulo operator (`%2 == 0` for even). We can then increment the corresponding counter (either `even` or `odd`) and then remove the last digit from the integer by using integer division (`/=`).

Finally, we return a tuple containing the counts of even and odd digits.

For example, if we call the function with the input `-12`, the function will iterate through each digit, and the counters will be incremented as follows: `even = 1` and `odd = 0`. If we call the function with the input `123`, the function will iterate through each digit, and the counters will be incremented as follows: `even = 1` and `odd = 2`. Therefore, the function will return the tuple `(1, 1)` for the input `-12` and the tuple `(1, 2)` for the input `123`.