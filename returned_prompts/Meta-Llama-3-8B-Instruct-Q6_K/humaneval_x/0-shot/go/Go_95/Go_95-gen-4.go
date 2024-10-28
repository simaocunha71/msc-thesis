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
        switch k.(type) {
        case string:
            if strings.ToLower(string(k)) == string(k) {
                allLower = true
            } else if strings.ToUpper(string(k)) == string(k) {
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

The function `CheckDictCase` takes a dictionary as input and checks if all keys are strings in lower case or all keys are strings in upper case. If the dictionary is empty, it returns `false`. 

It iterates over all keys in the dictionary. If a key is a string, it checks if it's in lower case or upper case. If it finds a key that is neither in lower case nor in upper case, it immediately returns `false`. 

If it checks all keys without finding any that are neither in lower case nor in upper case, it returns `true` if it found any keys in lower case or upper case, or `false` if it didn't find any. 

The function uses the `strings.ToLower` and `strings.ToUpper` functions to convert the keys to lower case and upper case, respectively. 

The function also uses a type switch to check the type of each key. If a key is not a string, it returns `false`. 

The function returns `allLower || allUpper` which is `true` if all keys are in lower case or all keys are in upper case, and `false` otherwise. 