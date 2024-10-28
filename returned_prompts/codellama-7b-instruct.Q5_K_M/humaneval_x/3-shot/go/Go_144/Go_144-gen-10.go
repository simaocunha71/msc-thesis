    x_numerator, _ := strconv.Atoi(strings.Split(x, "/")[0])
    x_denominator, _ := strconv.Atoi(strings.Split(x, "/")[1])

    n_numerator, _ := strconv.Atoi(strings.Split(n, "/")[0])
    n_denominator, _ := strconv.Atoi(strings.Split(n, "/")[1])

    result := x_numerator * n_denominator
    result2 := x_denominator * n_numerator

    if result == result2 {
        return true
    }else{
        return false
    }
}



