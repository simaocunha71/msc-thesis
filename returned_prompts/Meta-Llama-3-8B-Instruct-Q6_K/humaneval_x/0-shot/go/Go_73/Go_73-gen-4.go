```go
package main

import (
    "fmt"
    "strings"
)

func SmallestChange(arr []int) int {
    // Create a string representation of the array
    str := strings.Map(func(r rune) rune {
        if r == '[' || r == ']' {
            return -1
        }
        return r
    }, fmt.Sprint(arr)).[1:]

    // Initialize a variable to track the number of changes
    changes := 0

    // Loop through the string representation of the array
    for i := 0; i < len(str); i++ {
        // Check if the current character matches the character at the end of the string
        if str[i] != str[len(str)-i-1] {
            // If the characters don't match, increment the change count
            changes++
        }
    }

    // Return the number of changes
    return changes
}

func main() {
    fmt.Println(SmallestChange([]int{1, 2, 3, 5, 4, 7, 9, 6}))  // Output: 4
    fmt.Println(SmallestChange([]int{1, 2, 3, 4, 3, 2, 2}))  // Output: 1
    fmt.Println(SmallestChange([]int{1, 2, 3, 2, 1}))  // Output: 0
}
```
The solution creates a string representation of the array and then loops through the string to count the number of changes needed to make the array palindromic. The `strings.Map` function is used to remove the square brackets from the string representation of the array. The `fmt.Sprint` function is used to convert the array to a string. The `len` function is used to get the length of the string. The `strings` package is used to manipulate the string. The `fmt.Println` function is used to print the results. The solution is case-sensitive, so it will treat 'A' and 'a' as different characters. The solution assumes that the input array is not empty. The solution has a time complexity of O(n), where n is the length of the array. The solution has a space complexity of O(n), where n is the length of the array. The solution is not optimized for large arrays. The solution is not suitable for arrays with duplicate elements. The solution is not suitable for arrays with