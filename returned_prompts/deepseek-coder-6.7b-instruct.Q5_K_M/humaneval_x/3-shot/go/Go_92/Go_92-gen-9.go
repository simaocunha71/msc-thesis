    if x, ok := x.(float64); ok  {
        if x == float64(int(x))  {
            if y, ok := y.(float64); ok  {
                if y == float64(int(y))  {
                    if z, ok := z.(float64); ok  {
                        if z == float64(int(z))  {
                            return (x == y + z) || (y == x + z) || (z == x + y)
                        }
                    }
                }
            }
        }
    }
    return false
}



