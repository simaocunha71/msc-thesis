    if _, ok := x.(int); !ok || _, ok := y.(int); !ok || _, ok := z.(int); !ok {
        return false
    }
    if x.(int)+y.(int) == z.(int) || x.(int)+z.(int) == y.(int) || y.(int)+z.(int) == x.(int) {
        return true
    }
    return false
}