    xVal, ok := x.(float64)
    yVal, ok := y.(float64)
    zVal, ok := z.(float64)
    if !ok {
        return false
    }
    if xVal+yVal == zVal {
        return true
    }
    return false
}