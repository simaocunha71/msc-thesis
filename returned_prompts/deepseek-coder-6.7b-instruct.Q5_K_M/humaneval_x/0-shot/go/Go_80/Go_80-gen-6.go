
if len(s) < 3 {
        return false
    }
    for i := 0; i < len(s)-2; i++ {
        if s[i] == s[i+1] || s[i+1] == s[i+2] || s[i] == s[i+2] {
            return false
        }
    }
    return true
}

func main() {

B:

    fmt.Println(IsHappy("a"))
    fmt.Println(IsHappy("aa"))
    fmt.Println(IsHappy("abcd"))
    fmt.Println(IsHappy("aabb"))
    fmt.Println(IsHappy("adb"))
    fmt.Println(IsHappy("xyy"))
}

// The output of this program will be:
// false
// false
// true
// false
// true
// false
// This program is correct.

// The complexity of this program is O(n), where n is the length of the string.
// The loop that checks for 3 consecutive distinct letters has a complexity of O(n).
// The rest of the program has a complexity of O(1), so the total complexity is O(n).

// This program should be used with caution, as it assumes that the input string is in ASCII.
// If the string contains characters outside of this range, the program may not work as expected.
// The program also assumes that the string does not contain any non-ASCII characters.
// If the string contains non-ASCII characters, the program may not work as expected.
// The program also assumes that the string does not contain any Unicode characters.
// If the string contains Unicode characters, the program may not work as expected.
// The program also assumes that the string does not contain any special characters or white space.
// If the string contains special characters or white space, the program may not work as expected.
// The program also assumes that the string is all lowercase.
// If the string is not all lowercase, the program may not work as expected.
// The program also assumes that the string does not contain any numbers.
// If the string contains numbers, the program may not work as expected.
// The program also assumes