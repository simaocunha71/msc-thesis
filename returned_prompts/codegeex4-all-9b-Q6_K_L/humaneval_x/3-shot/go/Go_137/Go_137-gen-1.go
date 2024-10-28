    var a_num float64
    var b_num float64

    switch a.(type) {
    case string:
        a_num, _ = strconv.ParseFloat(a.(string), 64)
    case float64:
        a_num = a.(float64)
    case int:
        a_num = float64(a.(int))
    }

    switch b.(type) {
    case string:
        b_num, _ = strconv.ParseFloat(b.(string), 64)
    case float64:
        b_num = b.(float64)
    case int:
        b_num = float64(b.(int))
    }

    if a_num > b_num {
        return a
    } else if b_num > a_num {
        return b
    } else {
        return nil
    }
}

fmt.Println(CompareOne(1, 2.5)) // 2.5
fmt.Println(CompareOne(1, "2,3")) // "2,3"
fmt.Println(CompareOne("5,1", "6")) // "6"
fmt.Println(CompareOne("1", 1)) // nil
fmt.Println(CompareOne(1, "1")) // nil

