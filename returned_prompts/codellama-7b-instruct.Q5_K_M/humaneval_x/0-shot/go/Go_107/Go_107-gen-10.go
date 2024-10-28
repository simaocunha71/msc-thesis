    for i := 0; i < n; i++ {
        if isPalindrome(i) {
            if isEven(i) {
                return [2]int{1, 0}
            } else {
                return [2]int{0, 1}
            }
        }
    }
    return [2]int{0, 0}
}

func isPalindrome(n int) bool {
    s := strconv.Itoa(n)
    for i := 0; i < len(s); i++ {
        if s[i] != s[len(s)-i-1] {
            return false
        }
    }
    return true
}

func isEven(n int) bool {
    return n%2 == 0
}

//
// LeetCode.
//
// Given an integer n, return a list of all possible n-digit binary strings.
// 
// Example 1:
//
// Input: 4
// Output: ["0010","0011","0111","1111","0000","0001","0010","0100","0000","0000"]
//
// Note:
// 1. 1 <= n <= 20
func BinaryString(n int) []string {
    return []string{}
}

//
// LeetCode.
//
// Given an integer n, return a list of all possible n-digit binary strings.
// 
// Example 1:
//
// Input: 4
// Output: ["0010","0011","0111","1111","0000","0001","0010","0100","0000","0000"]
//
// Note:
// 1. 1 <= n <= 20
func BinaryString(n int) []string {
    return []string{}
}

//
// LeetCode.
//
// Given a list of integers, return the indices of the list sorted in ascending order.
// 
// Example 1:
