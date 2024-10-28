    if x, ok := x.(float64); ok {
        if y, ok := y.(float64); ok {
            if z, ok := z.(float64); ok {
                if x == float64(int(x)) && y == float64(int(y)) && z == float64(int(z)) {
                    return x == y+z || y == x+z || z == x+y
                }
            }
        }
    }
    return false
}



