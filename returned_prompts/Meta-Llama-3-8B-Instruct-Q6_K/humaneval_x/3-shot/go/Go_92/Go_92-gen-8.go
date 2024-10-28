    if xInt, ok := x.(int); ok {
        if yInt, ok := y.(int); ok {
            if zInt, ok := z.(int); ok {
                if xInt+yInt == zInt || xInt+zInt == yInt || yInt+zInt == xInt {
                    return true
                }
            }
        }
    }
    return false
} 