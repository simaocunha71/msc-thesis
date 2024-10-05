    if x, ok := x.(int); ok {
        if y, ok := y.(int); ok {
            if z, ok := z.(int); ok {
                return x+y==z || x+z==y || y+z==x
            }
        }
    }
    return false
}



