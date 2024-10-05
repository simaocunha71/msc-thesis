Here is the solution in Golang:
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
    for key := range dict {
        keyStr := strings.ToLower(fmt.Sprintf("%v", key))
        if !strings.EqualFold(keyStr, fmt.Sprintf("%v", key)) {
            allLower = false
        }
        keyStr = strings.ToUpper(fmt.Sprintf("%v", key))
        if !strings.EqualFold(keyStr, fmt.Sprintf("%v", key)) {
            allUpper = false
        }
    }
    return allLower || allUpper
}
```
Explanation:
The function `CheckDictCase` takes a map of type `map[interface{}]interface{}` as input. It first checks if the map is empty, if so, it returns `false`.

Then it initializes two boolean variables `allLower` and `allUpper` to `true`. These variables will be used to track whether all keys in the map are in lower case or upper case, respectively.

It then iterates over the keys in the map using a range loop. For each key, it converts the key to both lower case and upper case using the `strings.ToLower` and `strings.ToUpper` functions, respectively. It then checks if the original key and the converted key are equal using the `strings.EqualFold` function, which is case-insensitive. If the keys are not equal, it sets `allLower` or `allUpper` to `false`, depending on whether the key was converted to lower case or upper case.

Finally, the function returns `true` if either `allLower` or `allUpper` is `true`, indicating that all keys in the map are in either lower case or upper case. Otherwise, it returns `false`.