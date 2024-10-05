    numerator, _ := strconv.Atoi(strings.Split(x, "/")[0])
    denominator, _ := strconv.Atoi(strings.Split(x, "/")[1])

    other_numerator, _ := strconv.Atoi(strings.Split(n, "/")[0])
    other_denominator, _ := strconv.Atoi(strings.Split(n, "/")[1])

    if numerator * other_denominator % other_numerator == 0 {
        return true
    }else{
        return false
    }
}



