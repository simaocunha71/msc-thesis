    var (
        evens int
        odds  int
    )

B:
    for i := 1; i <= n; i++ {
        if isPalindrome(i) {
            if i%2 == 0 {
                evens++
            } else {
                odds++
            }
        }
    }

    return [2]int{evens, odds}
}

func isPalindrome(n int) bool {
    str := strconv.Itoa(n)
    for i := 0; i < len(str)/2; i++ {
        if str[i] != str[len(str)-i-1] {
            return false
        }
    }
    return true
}

// Time complexity: O(n*m) where n is the upper limit of the range and m is the number of digits in the number.
// Space complexity: O(1), constant space.

// This program calculates the number of even and odd palindromes in a given range. It does this by iterating over the range and checking each number to see if it's a palindrome. If it is, it checks whether the number is even or odd and increments the corresponding counter. Finally, it returns a tuple containing the counts of even and odd palindromes.

// The helper function isPalindrome checks whether a given number is a palindrome by converting it to a string and comparing the string to its reverse. It does this by iterating over the string and comparing each character to its corresponding character from the end of the string. If it finds any pair of characters that don't match, it returns false. If it gets through the entire string without finding any such pair, it returns true.

// The main function EvenOddPalindrome takes an integer n as input and returns a tuple containing the number of even and odd palindromes in the range from 1 to n, inclusive. It uses a loop to iterate over the range and the helper function isPalindrome to check each number. If a number is a palindrome, it checks whether it's even or odd and increments the corresponding counter. Finally, it returns the counts of even and odd palindromes as a tuple.

// This program