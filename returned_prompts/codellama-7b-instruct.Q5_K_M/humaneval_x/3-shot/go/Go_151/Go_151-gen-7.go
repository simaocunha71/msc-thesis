    var sum_of_odd_squares int = 0
    for _, v := range lst {
        if v >= 0 && math.Mod(v,1) == 0 {
            sum_of_odd_squares += int(v * v)
        }
    }
    return sum_of_odd_squares
}



