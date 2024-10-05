    switch a.(type) {
    case float64:
        if b.(float64) > a.(float64) {
            return b
        } else if b.(float64) < a.(float64) {
            return a
        } else {
            return nil
        }
    case int:
        if b.(int) > a.(int) {
            return b
        } else if b.(int) < a.(int) {
            return a
        } else {
            return nil
        }
    case string:
        if _, ok := b.(float64); ok {
            return CompareOne(strconv.ParseFloat(a.(string), 64), b)
        } else if _, ok := b.(int); ok {
            return CompareOne(strconv.ParseInt(a.(string), 10, 64), b)
        } else {
            if b.(string) > a.(string) {
                return b
            } else if b.(string) < a.(string) {
                return a
            } else {
                return nil
            }
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



































































































































































