    if xInt, ok := x.(int); ok && yInt, ok := y.(int); ok && zInt, ok := z.(int); ok {
        if xInt+yInt == zInt || xInt+zInt == yInt || yInt+zInt == xInt {
            return true
        }
    }
    return false
}