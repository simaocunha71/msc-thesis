    a_string := fmt.Sprintf("%v", a)
    b_string := fmt.Sprintf("%v", b)

    a_float, err1 := strconv.ParseFloat(strings.Replace(a_string, ",", ".", -1), 64)
    b_float, err2 := strconv.ParseFloat(strings.Replace(b_string, ",", ".", -1), 64)

    if err1 != nil || err2 != nil {
        return nil
    }

    if a_float == b_float {
        return nil
    } else if a_float > b_float {
        return a
    } else {
        return b
    }
}



