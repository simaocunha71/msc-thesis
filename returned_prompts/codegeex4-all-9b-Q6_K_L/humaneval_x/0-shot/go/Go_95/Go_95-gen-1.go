Here is the solution in Go:

```go
func CheckDictCase(dict map[interface{}]interface{}) bool {
    if len(dict) == 0 {
        return false
    }
    
    var upper bool
    for k := range dict {
        if _, ok := k.(string); !ok {
            return false
        }
        if strings.ToUpper(k.(string)) != k.(string) {
            if upper {
                return false
            }
        } else {
            upper = true
        }
    }
    return true
}
```

This function first checks if the dictionary is empty. If it is, it returns false. Then it iterates over the dictionary's keys. If any of the keys is not a string, it returns false. If the key is a string, it checks if it is in upper case. If it is, it sets a boolean flag `upper` to true. If the key is not in upper case and `upper` is already true, it returns false. If it completes the loop without returning false, it returns true.