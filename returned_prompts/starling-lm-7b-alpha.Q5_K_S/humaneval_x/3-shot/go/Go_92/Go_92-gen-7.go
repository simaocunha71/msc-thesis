    if _, ok := x.(float64); ok {
        return false
    }
    if _, ok := y.(float64); ok {
        return false
    }
    if _, ok := z.(float64); ok {
        return false
    }

    xi, yi, zi int
    if xi, ok = x.(int); !ok {
        return false
    }
    if yi, ok = y.(int); !ok {
        return false
    }
    if zi, ok = z.(int); !ok {
        return false
    }

    return (xi+yi==zi || yi+zi==xi || zi+xi==yi)
}



