
// Circular shift the digits of the integer x, shift the digits right by shift
// and return the result as a string.
// If shift > number of digits, return digits reversed.
// >>> CircularShift(12, 1)
// "21"
// >>> CircularShift(12, 2)
// "12"
func CircularShift(x int,shift int) string {
    // convert to a string
    s := strconv.Itoa(x)
    // get the number of digits
    n := len(s)
    // check if we need to reverse
    if shift > n {
        // reverse the string
        s = ReverseString(s)
    } else {
        // copy the first shift characters to the end
        s = s[:shift] + s[shift:]
        // reverse the remainder
        s = ReverseString(s)
    }
    // return the string
    return s
}

// Reverse the characters in a string
// >>> ReverseString("hello")
// "olleh"
func ReverseString(s string) string {
    // create a new byte array
    b := []byte(s)
    // reverse the bytes
    Reverse(b)
    // return the string
    return string(b)
}

// Reverse the bytes in a byte array
// >>> b := []byte("hello")
// >>> Reverse(b)
// "olleh"
func Reverse(b []byte) {
    // loop from the start to the end
    for i, j := 0, len(b)-1; i < j; {
        // swap the bytes
        b[i], b[j] = b[j], b[i]
        // move to the next pair of bytes
        i++
        j--
    }
}

// Check to see if a string is a palindrome
// >>> IsPalindrome("racecar")
// true
// >>> IsPalindrome("level")
// false
func IsPalindrome(s string) bool {
    // convert the string to a byte array
    b := []byte(s)
    // reverse the byte array
    Reverse