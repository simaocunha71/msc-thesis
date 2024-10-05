    if x_int, ok := x.(int); ok {
        if y_int, ok := y.(int); ok {
            if z_int, ok := z.(int); ok {
                return x_int + y_int == z_int || x_int + z_int == y_int || y_int + z_int == x_int
            }
        }
    }
    return false
}

I have tried to solve these problems but failed to solve them. So, I am asking for the help of the community.

A: 
