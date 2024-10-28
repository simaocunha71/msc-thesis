    if x_val, ok := x.(int); ok {
        if y_val, ok := y.(int); ok {
            if z_val, ok := z.(int); ok {
                return x_val == y_val+z_val || y_val == x_val+z_val || z_val == x_val+y_val
            }
        }
    }
    return false
}



