Here is the solution:
```go
import (
    "strings"
)

func CheckDictCase(dict map[interface{}]interface{}) bool {
    if len(dict) == 0 {
        return false
    }
    var allLower, allUpper bool
    for key, _ := range dict {
        keyStr := strings.ToLower(fmt.Sprintf("%v", key))
        if strings.ToUpper(keyStr) != keyStr {
            return false
        }
        if strings.ToLower(keyStr) != keyStr {
            allLower = false
        } else {
            allLower = true
        }
    }
    return allLower || allUpper
}
```
Explanation:
We first check if the dictionary is empty. If it is, we return false. Then we initialize two boolean variables, `allLower` and `allUpper`, to track whether all keys are in lower case or upper case, respectively.

We then iterate over the dictionary using the `range` keyword. For each key, we convert it to a string using `fmt.Sprintf` and then convert it to lower case using `strings.ToLower`. If the lower case version is different from the original key, it means the key is not in lower case, so we set `allLower` to false.

If the lower case version is the same as the original key, it means the key is in lower case, so we set `allLower` to true. We also set `allUpper` to true if `allLower` is true.

Finally, we return `allLower` or `allUpper`, whichever is true. If neither is true, it means the dictionary contains a mix of lower and upper case keys, so we return false. If both are true, it means the dictionary contains only lower case or only upper case keys, so we return true.