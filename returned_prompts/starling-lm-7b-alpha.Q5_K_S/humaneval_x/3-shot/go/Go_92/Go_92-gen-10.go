    if _,ok := x.(float64); ok {
        return false
    }
    if _,ok := y.(float64); ok {
        return false
    }
    if _,ok := z.(float64); ok {
        return false
    }
    if x.(int) + y.(int) == z.(int) {
        return true
    }
    if x.(int) + z.(int) == y.(int) {
        return true
    }
    if y.(int) + z.(int) == x.(int) {
        return true
    }
    return false
}



