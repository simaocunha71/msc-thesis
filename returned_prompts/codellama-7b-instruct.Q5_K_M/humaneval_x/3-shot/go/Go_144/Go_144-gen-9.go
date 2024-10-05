    x_numerator, x_denominator, err1 := strconv.Atoi(strings.Split(x, "/")[0])
    x_denominator, err2 := strconv.Atoi(strings.Split(x, "/")[1])
    n_numerator, n_denominator, err3 := strconv.Atoi(strings.Split(n, "/")[0])
    n_denominator, err4 := strconv.Atoi(strings.Split(n, "/")[1])

    if err1 != nil || err2 != nil || err3 != nil || err4 != nil{
        return false
    }

    if x_numerator*n_denominator == n_numerator*x_denominator{
        return true
    }else{
        return false
    }
}



