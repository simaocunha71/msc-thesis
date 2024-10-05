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
        if _, ok := key.(string); !ok {
            return false
        }
        if strings.ToLower(string(key.(string))) != string(key.(string)) {
            allLower = false
        }
        if strings.ToUpper(string(key.(string))) != string(key.(string)) {
            allUpper = false
        }
    }
    return allLower || allUpper
}
```

Explanation:
This function checks if all keys in the given dictionary are either in lower case or in upper case. If the dictionary is empty, the function returns false. 

First, we check if the dictionary is empty. If it is, we return false.

Then, we initialize two boolean variables, `allLower` and `allUpper`, to true. This means initially, we assume all keys are either in lower case or in upper case.

We iterate over each key in the dictionary. For each key, we check if it's a string. If it's not a string, we return false, because the dictionary should only contain strings as keys.

For each key, we convert it to a string and check if the lower case version of the string is the same as the original string. If not, we set `allLower` to false. We do the same for the upper case version of the string and `allUpper`.

Finally, we return `allLower || allUpper`, which means if all keys are either in lower case or in upper case, we return true; otherwise, we return false. 

This function handles dictionaries with both string and non-string keys, but it will return false if the dictionary contains non-string keys. 

The time complexity of this function is O(n), where n is the number of keys in the dictionary. The space complexity is O(1), which means the space required does not change with the size of the input dictionary. 