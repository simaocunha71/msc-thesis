    if len(arr) == 0 {
        return nil
    }

    var prod int = 1
    var sum float64 = 0

    for i := 0; i < len(arr); i++ {
        if arr[i] < 0 {
            prod *= -1
        } else if arr[i] == 0 {
            return 0
        }
        sum += math.Abs(float64(arr[i]))
    }

    return sum * float64(prod)
}



