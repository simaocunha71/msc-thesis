    if x, ok := x.(int); !ok || y, ok := y.(int); !ok || z, ok := z.(int); !ok {
        return false
    }
    if x+y == z || x+z == y || y+z == x {
        return true
    }
    return false
}