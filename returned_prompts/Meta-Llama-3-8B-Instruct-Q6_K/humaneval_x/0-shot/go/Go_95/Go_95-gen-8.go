Here is the solution to the problem:

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
    for key := range dict {
        s := strings.ToLower(fmt.Sprint(key))
        if strings.ToUpper(s) != s {
            allLower = false
        } else {
            allUpper = true
        }
    }
    return allLower || allUpper
}
```

This function checks if all keys in the given dictionary are either in lower case or upper case. If the dictionary is empty, it returns false. It iterates over the dictionary and checks each key. If any key is not in either lower case or upper case, it sets the `allLower` and `allUpper` variables to false. At the end, it returns true if either `allLower` or `allUpper` is true, indicating that all keys are in either lower case or upper case. Otherwise, it returns false.