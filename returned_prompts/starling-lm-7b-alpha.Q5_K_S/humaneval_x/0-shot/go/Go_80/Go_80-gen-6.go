
Here's a detailed breakdown of the solution:

1. Initialize a map to store the last three characters of the string as a key and the count of the occurrence of the last three characters as a value. This map will be used to keep track of the occurrence of the last three characters.

2. Initialize a variable "res" as true to denote that the string is happy.

3. Iterate through the string using a for loop starting from index 2. This is because the first three characters are considered as a starting point and are not part of the consecutive three characters check.

4. Inside the loop, check if the last three characters (s[i-2:i]) are present in the map. If they are present, it means that the consecutive three characters are not distinct. In this case, set "res" to false and break out of the loop.

5. If the last three characters are not present in the map, add them as a key with a value of 1 to the map.

6. After the loop, check if the length of the string is less than 3 or "res" is false. If any of these conditions is true, return false, indicating that the string is not happy.

7. Otherwise, return true, indicating that the string is happy.

The provided code implements the above solution and returns the result of whether the string is happy or not.

Here's the code:

```go
package main

import "fmt"

func IsHappy(s string) bool {
    m := make(map[string]int)
    res := true

    for i := 2; i < len(s); i++ {
        if _, ok := m[s[i-2:i]]; ok {
            res = false
            break
        }
        m[s[i-2:i]] = 1
    }

    if len(s) < 3 || !res {
        return false
    }
    return true
}

func main() {
    fmt.Println(IsHappy("a"))        // false
    fmt.Println(IsHappy("aa"))       // false
    fmt.Println(IsHappy("abcd"))     // true
    fmt.Println(Is