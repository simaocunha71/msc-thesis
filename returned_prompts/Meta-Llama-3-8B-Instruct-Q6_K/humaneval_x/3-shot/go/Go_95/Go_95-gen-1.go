    var allLower bool = true
    var allUpper bool = true

    for _, value := range dict {
        key := fmt.Sprintf("%s", dict.keys()[0])
        if strings.ToLower(key) != key {
            allLower = false
        }
        if strings.ToUpper(key) != key {
            allUpper = false
        }
    }
    return (allLower && len(dict) > 0) || (allUpper && len(dict) > 0)
}
// Error: dict.keys() is undefined. You can use range to iterate over the keys of the dictionary.
// You can convert interface{} to string using fmt.Sprintf("%s", interface{}).
// You can use strings.ToLower() and strings.ToUpper() to check if the string is in lower case or upper case.
// You can use && operator to check if all the keys are in lower case or upper case.
// You can use || operator to check if the dictionary is not empty.