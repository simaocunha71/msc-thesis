    switch a.(type) {
    case int:
        switch b.(type) {
        case float64:
            return b
        case string:
            b = strings.Replace(b.(string), ",", ".", -1)
            b, _ := strconv.ParseFloat(b.(string), 64)
            if float64(a.(int)) < b {
                return b
            }
        }
    case float64:
        switch b.(type) {
        case int:
            if a.(float64) < float64(b.(int)) {
                return b
            }
        case string:
            b = strings.Replace(b.(string), ",", ".", -1)
            b, _ := strconv.ParseFloat(b.(string), 64)
            if a.(float64) < b {
                return b
            }
        }
    case string:
        a = strings.Replace(a.(string), ",", ".", -1)
        a, _ := strconv.ParseFloat(a.(string), 64)
        switch b.(type) {
        case int:
            if a.(float64) > float64(b.(int)) {
                return a
            }
        case float64:
            if a.(float64) > b.(float64) {
                return a
            }
        case string:
            b = strings.Replace(b.(string), ",", ".", -1)
            b, _ := strconv.ParseFloat(b.(string), 64)
            if a.(float64) > b {
                return a
            }
        }
    }

    return nil
}

I'm new to Golang and programming in general, I'm trying to understand why this code is not working as expected. 
It seems like the code is not detecting the types correctly. I'm not sure why that's happening.

A: The issue is in the last case where b is a string. You're parsing a as a float64 and checking if a is greater than b, which makes no sense as b is a string.
You're