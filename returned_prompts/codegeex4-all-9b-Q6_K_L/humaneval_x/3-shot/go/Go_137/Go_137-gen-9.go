    a_str := fmt.Sprintf("%v",a)
    b_str := fmt.Sprintf("%v",b)

    a_float, _ := strconv.ParseFloat(a_str, 64)
    b_float, _ := strconv.ParseFloat(b_str, 64)

    if a_float > b_float {
        return a
    } else if a_float < b_float {
        return b
    } else {
        return nil
    }
}



