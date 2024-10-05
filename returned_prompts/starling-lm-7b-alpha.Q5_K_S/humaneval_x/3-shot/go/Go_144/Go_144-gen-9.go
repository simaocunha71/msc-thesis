    numerator_x, _ := strconv.Atoi(strings.Split(x,"/")[0])
    denominator_x, _ := strconv.Atoi(strings.Split(x,"/")[1])
    numerator_n, _ := strconv.Atoi(strings.Split(n,"/")[0])
    denominator_n, _ := strconv.Atoi(strings.Split(n,"/")[1])

    if (numerator_n * denominator_x) % denominator_n == 0 {
        return true
    }
    return false
}



