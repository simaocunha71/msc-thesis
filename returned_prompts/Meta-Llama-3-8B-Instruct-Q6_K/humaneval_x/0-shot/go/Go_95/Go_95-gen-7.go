Here is the solution in Go:
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
    for _, key := range dict {
        keyStr := fmt.Sprintf("%v", key)
        if strings.ToLower(keyStr) == keyStr {
            allLower = true
        } else if strings.ToUpper(keyStr) == keyStr {
            allUpper = true
        } else {
            return false
        }
    }
    return allLower || allUpper
}
```
Explanation:

1. First, we check if the dictionary is empty. If it is, we return false.
2. We initialize two boolean variables, `allLower` and `allUpper`, to track whether all keys are in lower case or upper case.
3. We iterate over the keys in the dictionary using the `range` keyword.
4. For each key, we convert it to a string using `fmt.Sprintf("%v", key)`.
5. We check if the string is in lower case using `strings.ToLower(keyStr) == keyStr`. If it is, we set `allLower` to true.
6. We check if the string is in upper case using `strings.ToUpper(keyStr) == keyStr`. If it is, we set `allUpper` to true.
7. If the key is neither in lower case nor upper case, we return false.
8. Finally, we return `allLower || allUpper`, which is true if all keys are in lower case or upper case, and false otherwise.