```go
func CheckDictCase(dict map[interface{}]interface{}) bool {
    keys := make([]string, 0, len(dict))
    for k := range dict {
        keys = append(keys, k.(string))
    }
    if len(keys) == 0 {
        return false
    }
    allLower := true
    allUpper := true
    for _, k := range keys {
        if !strings.EqualFold(k, strings.ToLower(k)) {
            allUpper = false
        }
        if !strings.EqualFold(k, strings.ToUpper(k)) {
            allLower = false
        }
    }
    return allLower || allUpper
}
```
