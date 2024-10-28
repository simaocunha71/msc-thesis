```go
func CompareOne(a, b interface{}) interface{} {
    switch a.(type) {
    case int:
        switch b.(type) {
        case int:
            if a.(int) > b.(int) {
                return a
            }
            if b.(int) > a.(int) {
                return b
            }
            return nil
        case float64:
            if float64(a.(int)) > b.(float64) {
                return a
            }
            if b.(float64) > float64(a.(int)) {
                return b
            }
            return nil
        case string:
            if float64(a.(int)) > strToFloat(b.(string)) {
                return a
            }
            if strToFloat(b.(string)) > float64(a.(int)) {
                return b
            }
            return nil
        }
    case float64:
        switch b.(type) {
        case int:
            if a.(float64) > float64(b.(int)) {
                return a
            }
            if float64(b.(int)) > a.(float64) {
                return b
            }
            return nil
        case float64:
            if a.(float64) > b.(float64) {
                return a
            }
            if b.(float64) > a.(float64) {
                return b
            }
            return nil
        case string:
            if a.(float64) > strToFloat(b.(string)) {
                return a
            }
            if strToFloat(b.(string)) > a.(float64) {
                return b
            }
            return nil
        }
    case string:
        switch b.(type) {
        case int:
            if strToFloat(a.(string)) > float64(b.(int)) {
                return a
            }
            if float64(b.(int)) > strToFloat(a.(string)) {
                return b
            }
            return nil
        case float64:
            if strToFloat(a.(string)) > b.(float64) {
                return a
            }
            if b.(float64) > strToFloat(a.(string)) {
                return b
            }
            return nil
        case string:
            if strToFloat(a.(string)) > strToFloat(b.(string)) {
                return a
            }
            if strToFloat(b.(string)) > strToFloat(a.(string)) {
