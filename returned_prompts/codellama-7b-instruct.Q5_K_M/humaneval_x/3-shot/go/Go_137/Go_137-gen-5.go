    if a == b{
        return nil
    }

    a_str := fmt.Sprintf("%v", a)
    b_str := fmt.Sprintf("%v", b)

    if strings.Contains(a_str, "."){
        a_float, _ := strconv.ParseFloat(a_str, 64)
        if a_float > b_str{
            return a
        }
    }else{
        a_int, _ := strconv.Atoi(a_str)
        if a_int > b_str{
            return a
        }
    }

    if strings.Contains(b_str, "."){
        b_float, _ := strconv.ParseFloat(b_str, 64)
        if b_float > a_str{
            return b
        }
    }else{
        b_int, _ := strconv.Atoi(b_str)
        if b_int > a_str{
            return b
        }
    }

    return nil
}



