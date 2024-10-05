    if len(arr) == 0 {
        return nil
    }

    result := math.Sign(arr[0])
    for i := 1; i < len(arr); i++ {
        if arr[i] == 0 {
            result *= 0
        }else {
            result *= math.Sign(arr[i])
        }
    }
    return math.Abs(result)
}



