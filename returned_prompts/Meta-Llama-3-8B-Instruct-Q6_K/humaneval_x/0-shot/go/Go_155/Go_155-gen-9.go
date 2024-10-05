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
Here is the explanation of the code:

1. We initialize two variables `even` and `odd` to 0, which will be used to count the number of even and odd digits respectively.
2. We use a for loop to iterate over each digit of the number. We use the modulus operator (`%`) to extract the last digit of the number. 
3. We check if the digit is even by using the modulus operator again (`% 2`). If the result is 0, it means the digit is even, so we increment the `even` variable. Otherwise, we increment the `odd` variable.
4. We use integer division (`/`) to remove the last digit from the number.
5. We repeat steps 2-4 until the number becomes 0.
6. Finally, we return a tuple (array of two integers) containing the count of even and odd digits.

The time complexity of this solution is O(logN) where N is the input number, because we are processing each digit of the number once. The space complexity is O(1) because we are using a constant amount of space to store the variables. 