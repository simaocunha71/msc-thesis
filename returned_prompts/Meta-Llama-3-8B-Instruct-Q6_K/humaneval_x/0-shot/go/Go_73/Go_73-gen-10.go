```go
package main

import (
    "fmt"
    "strings"
)

func SmallestChange(arr []int) int {
    // Convert the array to a string
    str := strings.Join(fmt.Sprint(arr), "")

    // Initialize the count of changes
    changes := 0

    // Initialize two pointers for the left and right ends of the string
    left, right := 0, len(str) - 1

    // Loop through the string until the two pointers meet
    for left < right {
        // If the characters at the left and right ends are different
        if str[left] != str[right] {
            // Increment the count of changes
            changes++
            // If the character at the left end is different from the character at the center
            if str[left] != str[len(str)-left-1] {
                // Move the left pointer to the right
                left++
            } else {
                // Move the right pointer to the left
                right--
            }
        } else {
            // If the characters at the left and right ends are the same
            // Move both pointers towards the center
            left++
            right--
        }
    }

    // Return the count of changes
    return changes
}

func main() {
    fmt.Println(SmallestChange([]int{1, 2, 3, 5, 4, 7, 9, 6})) // Output: 4
    fmt.Println(SmallestChange([]int{1, 2, 3, 4, 3, 2, 2})) // Output: 1
    fmt.Println(SmallestChange([]int{1, 2, 3, 2, 1})) // Output: 0
}
```

This program works by converting the input array to a string and then iterating through the string to find the minimum number of elements that need to be changed to make the array palindromic. It uses two pointers, one starting from the beginning of the string and one starting from the end, and moves them towards the center of the string. If the characters at the two pointers are different, it increments the count of changes and moves the pointer that points to the character that is closer to the center towards the center. If the characters at the two pointers are the same, it moves both pointers towards the center. The program returns the count of changes at the end.