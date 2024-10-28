
func CycpatternCheck(a , b string) bool {
    b = b + b
    return strings.Contains(a, b)
}

Explanation:
Here, we concatenate the string b with itself, thus creating all possible rotations of b. We then check if the resulting string contains a. This is equivalent to checking if b is a substring of a or if any rotation of b is a substring of a.

The time complexity of this solution is O(n + m), where n is the length of the first string and m is the length of the second string.

The space complexity of the solution is O(m).

This solution does not require the use of any additional packages or libraries beyond the core Go language.

*/

package main

import (
    "fmt"
    "strings"
)

func CycpatternCheck(a, b string) bool {
    b = b + b
    return strings.Contains(a, b)
}

func main() {
    fmt.Println(CycpatternCheck("abcd", "abd"))
    fmt.Println(CycpatternCheck("hello", "ell"))
    fmt.Println(CycpatternCheck("whassup", "psus"))
    fmt.Println(CycpatternCheck("abab", "baa"))
    fmt.Println(CycpatternCheck("efef", "eeff"))
    fmt.Println(CycpatternCheck("himenss", "simen"))
}





































































































































































