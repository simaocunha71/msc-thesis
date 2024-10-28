Here is the solution in Go:
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
    for _, key := range dict {
        switch key.(type) {
        case string:
            if !strings.EqualFold(string(key.(string)), string(key.(string))) {
                allLower = false
                allUpper = false
                break
            }
            if strings.ToLower(string(key.(string))) != string(key.(string)) {
                allLower = false
            }
            if strings.ToUpper(string(key.(string))) != string(key.(string)) {
                allUpper = false
            }
        default:
            return false
        }
    }
    return allLower || allUpper
}
```
This function iterates over the keys of the dictionary and checks if they are all in lower case or all in upper case. If any key is not a string or is not in the desired case, the function returns false. If the dictionary is empty, the function returns false. Otherwise, it returns true if all keys are in the same case. 

Here's a breakdown of the code:
- The function first checks if the dictionary is empty. If it is, it returns false.
- It then initializes two boolean variables, `allLower` and `allUpper`, to true. These variables will be used to track whether all keys are in lower case or upper case.
- The function then iterates over the keys of the dictionary using a range loop.
- For each key, it checks if the key is a string using a type switch. If the key is not a string, the function returns false.
- If the key is a string, it checks if the string is in lower case or upper case using the `strings.EqualFold` function, which is case-insensitive, and the `strings.ToLower` and `strings.ToUpper` functions, which convert the string to lower or upper case. If the string is not in the desired case, the function sets `allLower` or `allUpper` to false.
- If any key is not a string or is not in the desired case, the function returns false.
- If the function finishes iterating over the keys without finding any keys that are not in the desired case, it returns true if `allLower` or `allUpper` is still true, indicating that all keys are in