    switch {
    case x.(type) == int && y.(type) == int && z.(type) == int:
        if x.(int) == y.(int) + z.(int) {
            return true
        }
    case x.(type) == float64 && y.(type) == float64 && z.(type) == float64:
        if x.(float64) == y.(float64) + z.(float64) {
            return true
        }
    default:
        return false
    }
    return false
}



