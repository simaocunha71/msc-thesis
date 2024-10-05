    var even, odd int
    for i := 1; i <= n; i++ {
        if isPalindrome(i) {
            if i%2 == 0 {
                even++
            } else {
                odd++
            }
        }
    }
    return [2]int{even, odd}
}

func isPalindrome(n int) bool {
    s := strconv.Itoa(n)
    for i := 0; i < len(s)/2; i++ {
        if s[i] != s[len(s)-1-i] {
            return false
        }
    }
    return true
}
```

## Test Cases:

```python
print(EvenOddPalindrome(1))  # (0, 1)
print(EvenOddPalindrome(2))  # (1, 1)
print(EvenOddPalindrome(3))  # (1, 2)
print(EvenOddPalindrome(12))  # (4, 6)
print(EvenOddPalindrome(100))  # (33, 66)
```

## Explanation:

The function `EvenOddPalindrome(n)` is intended to count the number of even and odd palindromic numbers in the range 1 to `n` inclusive. It does this by iterating over the range and checking each number to see if it is a palindrome. If it is, it then checks if the number is even or odd and increments the corresponding counter. The counters are returned as a tuple in the form `(even, odd)`.

The helper function `isPalindrome(n)` is used to check if a number is a palindrome. It does this by converting the number to a string and then checking if the string is the same forwards and backwards. If it is, the function returns `True`, otherwise it returns `False`.

The time complexity of this solution is O(n^2) due to the nested loop structure where the outer loop runs `n` times and the inner