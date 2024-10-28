    var x1, y1, z1 int
    var ok bool
    if x1, ok = x.(int); !ok {
        return false
    }
    if y1, ok = y.(int); !ok {
        return false
    }
    if z1, ok = z.(int); !ok {
        return false
    }

    return x1 + y1 == z1 || x1 + z1 == y1 || y1 + z1 == x1
}



