Here is the solution:
```go
import (
    "strings"
)

func CheckDictCase(dict map[interface{}]interface{}) bool {
    if len(dict) == 0 {
        return false
    }
    var allLower bool
    var allUpper bool
    for k := range dict {
        switch v := k.(type) {
        case string:
            if strings.ToLower(v) == v {
                allLower = true
            } else if strings.ToUpper(v) == v {
                allUpper = true
            } else {
                return false
            }
        default:
            return false
        }
    }
    return allLower || allUpper
}
```
Here's an explanation of the solution:

1. First, we check if the dictionary is empty. If it is, we return false.
2. We then iterate over the keys of the dictionary using the range keyword.
3. For each key, we check its type using a type switch. If the key is a string, we check if it's in all lower case or all upper case using the `strings.ToLower` and `strings.ToUpper` functions.
4. If we find a key that's not a string or is not in all lower case or all upper case, we return false.
5. If we reach the end of the loop without returning false, we return true if either all keys were in all lower case or all keys were in all upper case.

Note that we use the `interface{}` type to represent the key and value types of the dictionary, since the problem statement doesn't specify the types of the dictionary. We then use the `switch` statement to check the type of the key and value and handle them accordingly. The `strings.ToLower` and `strings.ToUpper` functions are used to check if the key is in all lower case or all upper case. The `range` keyword is used to iterate over the keys of the dictionary. The `len` function is used to check if the dictionary is empty. The `return` statement is used to exit the function early if the dictionary is empty or if we find a key that doesn't match the desired case. The `||` operator is used to check if either all keys were in all lower case or all keys were in all upper case. The `bool` type is used to represent the result of the function. The `false` value is used to represent the result when the dictionary is empty or when we find a key that doesn't match the desired case.