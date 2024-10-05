```go
func CheckDictCase(dict map[interface{}]interface{}) bool {
    if len(dict) == 0 {
        return false
    }

    var allLower, allUpper bool
    for k := range dict {
        key, ok := k.(string)
        if !ok {
            return false
        }
        allLower = allLower && strings.ToLower(key) == key
        allUpper = allUpper && strings.ToUpper(key) == key
    }
    return allLower || allUpper
}
```