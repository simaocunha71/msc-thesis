    if _, ok := x.(int); !ok {
        return false
    }
    if _, ok := y.(int); !ok {
        return false
    }
    if _, ok := z.(int); !ok {
        return false
    }
    if x.(int)+y.(int) == z.(int) {
        return true
    }
    if x.(int)+z.(int) == y.(int) {
        return true
    }
    if y.(int)+z.(int) == x.(int) {
        return true
    }
    return false
}