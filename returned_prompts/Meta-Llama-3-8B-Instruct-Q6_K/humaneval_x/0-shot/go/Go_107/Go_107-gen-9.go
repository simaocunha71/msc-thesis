```go
func EvenOddPalindrome(n int) [2]int {
    even, odd := 0, 0
    for i := 1; i <= n; i++ {
        s := strconv.Itoa(i)
        if s == strconv.Itoa(i)[::-1] {
            if strconv.Itoa(i)[0] == '1' || strconv.Itoa(i)[0] == '3' || strconv.Itoa(i)[0] == '5' || strconv.Itoa(i)[0] == '7' || strconv.Itoa(i)[0] == '9' {
                odd++
            } else {
                even++
            }
        }
    }
    return [2]int{even, odd}
}
```


Explanation:
This function iterates over the range from 1 to n (inclusive), and for each number, it checks if it's a palindrome by converting it to a string and comparing it to its reverse. If it's a palindrome, it then checks if the first digit is an odd digit (1, 3, 5, 7, or 9), and if so, it increments the odd counter; otherwise, it increments the even counter. Finally, it returns a tuple containing the counts of even and odd palindromes.

The time complexity is O(n), where n is the input number, because we're iterating over the range from 1 to n. The space complexity is O(1), because we're using a constant amount of space to store the counters and other variables.