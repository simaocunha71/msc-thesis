Here is a simple solution for this problem:

```go
import (
    "strings"
)

func CheckDictCase(dict map[interface{}]interface{}) bool {
    if len(dict) == 0 {
        return false
    }
    allLower := true
    allUpper := true
    for k := range dict {
        switch k.(type) {
        case string:
            if !strings.EqualFold(k.(string), strings.ToLower(k.(string))) {
                allLower = false
            }
            if !strings.EqualFold(k.(string), strings.ToUpper(k.(string))) {
                allUpper = false
            }
        default:
            return false
        }
    }
    return allLower || allUpper
}
```

This function first checks if the dictionary is empty. If it is, the function returns false. Then it iterates over each key in the dictionary. If the key is a string, it checks if the key is either all lower case or all upper case. If the key is not a string, the function returns false. Finally, it returns whether the dictionary is either all lower case or all upper case. 

This function uses the `strings.EqualFold` function to check if two strings are equal, regardless of case. It uses the `strings.ToLower` and `strings.ToUpper` functions to convert a string to lower case and upper case, respectively. The `switch` statement is used to check the type of the key, and the `range` keyword is used to iterate over the keys in the dictionary. 

Note that this function assumes that the dictionary keys are not nil. If nil keys are allowed, additional checks are needed. 

Also, this function uses the `interface{}` type to represent the keys and values in the dictionary. This is because the problem statement does not specify the types of the keys and values. If the keys and values are known to be of certain types, the `interface{}` type can be replaced with those types. 