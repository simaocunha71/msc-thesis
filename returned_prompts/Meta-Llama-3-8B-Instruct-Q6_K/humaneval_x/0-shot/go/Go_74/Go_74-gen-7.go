Here is a Go function that does what you described:
```go
func TotalMatch(lst1 []string, lst2 []string) []string {
    totalChars1 := 0
    totalChars2 := 0
    for _, str := range lst1 {
        totalChars1 += len(str)
    }
    for _, str := range lst2 {
        totalChars2 += len(str)
    }
    if totalChars1 < totalChars2 {
        return lst1
    } else if totalChars2 < totalChars1 {
        return lst2
    } else {
        return lst1
    }
}
```
Here's an explanation of how the function works:

1. We initialize two variables `totalChars1` and `totalChars2` to 0. These variables will keep track of the total number of characters in each list.
2. We loop through each string in `lst1` and add its length to `totalChars1`.
3. We loop through each string in `lst2` and add its length to `totalChars2`.
4. We compare the two totals. If `totalChars1` is less than `totalChars2`, we return `lst1`. If `totalChars2` is less than `totalChars1`, we return `lst2`. If the two totals are equal, we return `lst1` (since the problem statement says to return the first list if the totals are equal).

You can test this function with the examples you provided to see that it produces the correct output. Let me know if you have any questions or if you'd like me to explain anything further! 😊

Example usage:
```go
package main

import "fmt"

func main() {
    fmt.Println(TotalMatch([]string{"hi", "admin"}, []string{"hI", "Hi"})) // Output: [hI Hi]
    fmt.Println(TotalMatch([]string{"hi", "admin"}, []string{"hi", "hi", "admin", "project"})) // Output: [hi admin]
    fmt.Println(TotalMatch([]string{"hi", "admin"}, []string{"hI", "hi", "hi"})) // Output: [hI hi hi]
    fmt.Println(TotalMatch([]string{"4"}, []string{"1", "2", "3", "4", "5"})) // Output: [4]
}
```