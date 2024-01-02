import (
    "strings"
)

// Given a dictionary, return true if all keys are strings in lower
// case or all keys are strings in upper case, else return false.
// The function should return false is the given dictionary is empty.
// Examples:
// CheckDictCase({"a":"apple", "b":"banana"}) should return true.
// CheckDictCase({"a":"apple", "A":"banana", "B":"banana"}) should return false.
// CheckDictCase({"a":"apple", 8:"banana", "a":"apple"}) should return false.
// CheckDictCase({"Name":"John", "Age":"36", "City":"Houston"}) should return false.
// CheckDictCase({"STATE":"NC", "ZIP":"12345" }) should return true.
func CheckDictCase(dict map[interface{}]interface{}) bool {
    if dict == nil || len(dict) <= 0 {
        return false
    }
    keys := make(map[string]bool, len(dict))
    for keyName, value := range dict {
        isLowerCase := strings.ToLower(keyName.(string))
        isUpperCase := strings.ToUpper(keyName.(string))
        if isLowerCase || isUpperCase {
            keys[strings.ToLower(keyName.(string))] = true
        } else {
            keys[""] = false
            return false
        }
    }
    for _, key := range keys {
        if !key {
            return false
        }
    }
    return true
}