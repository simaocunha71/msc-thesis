    if _, ok := x.(int); ok && _, ok := y.(int); ok && _, ok := z.(int); ok {
        return (x + y == z) || (x + z == y) || (y + z == x)
    }
    return false
}



