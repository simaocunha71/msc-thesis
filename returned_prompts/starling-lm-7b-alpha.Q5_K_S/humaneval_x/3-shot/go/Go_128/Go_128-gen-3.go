    if len(arr) == 0 {
        return nil
    }
    result := math.Significand(math.Copysign(1, arr[0]))
    for _, v := range arr[1:] {
        if v == 0 {
            return 0
        }
        result *= math.Significand(math.Copysign(1, v))
    }
    return result
}



