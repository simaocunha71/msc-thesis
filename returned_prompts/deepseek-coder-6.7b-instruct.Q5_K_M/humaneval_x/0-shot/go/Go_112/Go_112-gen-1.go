  for _, v := range c {
    s = strings.ReplaceAll(s, string(v), "")
  }

  return [2]interface{}{s, isPalindrome(s)}
}

func isPalindrome(s string) bool {
    return s == Reverse(s)
}

func Reverse(s string) string {
    runes := []rune(s)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}

// The time complexity of this function is O(n^2), because we use the strings.ReplaceAll() function inside a loop.
// The space complexity is O(n), because we create a new string for each character that we delete.
// Note: The Reverse function has a time complexity of O(n) and space complexity of O(n).

// The function ReverseDelete() first deletes all the characters in c from the string s, then checks if the result string is a palindrome.
// The function isPalindrome() checks if the given string is a palindrome by comparing it with its reverse.
// The function Reverse() reverses a string.

// The returned value is a tuple containing the result string and a boolean value indicating whether the string is a palindrome.
// If the string is a palindrome, the boolean value is true; otherwise, it's false.

// Test cases:
// fmt.Println(ReverseDelete("abcde", "ae")) // should return ("bcd", false)
// fmt.Println(ReverseDelete("abcdef", "b")) // should return ("acdef", false)
// fmt.Println(ReverseDelete("abcdedcba", "ab")) // should return ("cdedc", true)
// fmt.Println(ReverseDelete("deed", "ed")) // should return ("d", true)
// fmt.Println(ReverseDelete("aabbaa", "a")) // should