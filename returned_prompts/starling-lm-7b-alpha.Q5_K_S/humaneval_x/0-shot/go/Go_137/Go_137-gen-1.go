    aType := reflect.TypeOf(a)
    bType := reflect.TypeOf(b)

    if aType.Kind() == reflect.String && bType.Kind() == reflect.Float64 {
        if strings.Contains(a.(string), ".") {
            aFloat, err := strconv.ParseFloat(a.(string), 64)
            if err != nil {
                return nil
            }
            if aFloat > b.(float64) {
                return a
            } else {
                return b
            }
        } else {
            aFloat, err := strconv.ParseFloat(a.(string), 64)
            if err != nil {
                return nil
            }
            if aFloat > b.(float64) {
                return a
            } else {
                return b
            }
        }
    } else if aType.Kind() == reflect.String && bType.Kind() == reflect.String {
        if strings.Contains(a.(string), ".") {
            aFloat, err := strconv.ParseFloat(a.(string), 64)
            if err != nil {
                return nil
            }
            if aFloat > b.(float64) {
                return a
            } else {
                return b
            }
        } else {
            aFloat, err := strconv.ParseFloat(a.(string), 64)
            if err != nil {
                return nil
            }
            if aFloat > b.(float64) {
                return a
            } else {
                return b
            }
        }
    } else {
        if a.(float64) > b.(float64) {
            return a
        } else {
            return b
        }
    }
    return nil
}

func main() {
    fmt.Println(CompareOne(1, 2.5))
    fmt.Println(CompareOne(1, "2,3"))
    fmt.Println(CompareOne("5,1", "6"))
    fmt.Println(CompareOne("1", 1))
}




