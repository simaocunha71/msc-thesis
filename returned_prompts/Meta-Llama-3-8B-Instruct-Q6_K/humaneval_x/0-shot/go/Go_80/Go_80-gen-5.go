```go
package main
import "strings"
func IsHappy(s string) bool {
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
    fmt.Println(IsHappy("a")) // false
    fmt.Println(IsHappy("aa")) // false
    fmt.Println(IsHappy("abcd")) // true
    fmt.Println(IsHappy("aabb")) // false
    fmt.Println(IsHappy("adb")) // true
    fmt.Println(IsHappy("xyy")) // false
}
```



Explanation:

*   We first check if the length of the string is less than 3. If it is, we immediately return `false` because a happy string must have a length of at least 3.
*   We then iterate over the string using a for loop, checking every 3 consecutive characters.
*   Inside the loop, we use three if statements to check if the current character, the next character, or the character after the next is equal to any of the other two. If any of these conditions are true, we return `false` because the string is not happy.
*   If we finish the loop without finding any duplicates, we return `true` because the string is happy.

The `main` function is used to test the `IsHappy` function with different inputs and print the results.