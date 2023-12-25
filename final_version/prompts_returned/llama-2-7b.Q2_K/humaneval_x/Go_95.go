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
    if dict == nil || len(dict) < 1 {
        return false
    }

    i := ""
    for k, v := range dict {
        switch strings.ToLower(k)[0:1] {
            case "a":
                if !strings.EqualFold(v.(string), "apple") {
                    return false
                } else {
                    i = strings.ToLower(k)
                }
            case "b":
                if !strings.EqualFold(v.(string), "banana") {
                    return false
                } else {
                    i = strings.ToUpper(k)
                }
        }
    }

    if strings.HasPrefix(i, "A" | "B") && !strings.EqualFold(v.(string), "banana") {
        return false
    } else {
        return true
    }
}
