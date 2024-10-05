```go
func EvenOddPalindrome(n int) [2]int {
    even, odd := 0, 0
    for i := 1; i <= n; i++ {
        str := strconv.Itoa(i)
        if str == strconv.Itoa(i)[::-1] {
            if i%2 == 0 {
                even++
            } else {
                odd++
            }
        }
    }
    return [2]int{even, odd}
}
```
The solution uses a simple loop to iterate over all numbers from 1 to n, converts each number to a string, checks if the string is a palindrome (i.e., equals its reverse), and increments either the even or odd count accordingly. The final result is returned as a tuple of two integers. 

Time complexity: O(n)
Space complexity: O(1) (since we are not using any extra space that scales with input size) 