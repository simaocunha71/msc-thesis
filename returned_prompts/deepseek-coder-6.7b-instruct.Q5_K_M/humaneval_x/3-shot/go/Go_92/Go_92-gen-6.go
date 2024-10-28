    switch x := x.(type) {
    case float64:
        return false
    case int:
        switch y := y.(type) {
        case float64:
            return false
        case int:
            switch z := z.(type) {
            case float64:
                return false
            case int:
                return (x == y+z) || (y == x+z) || (z == x+y)
            }
        }
    }
    return false
}



