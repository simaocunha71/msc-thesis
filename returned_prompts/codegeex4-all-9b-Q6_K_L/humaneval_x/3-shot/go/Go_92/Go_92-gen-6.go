    x_ := x.(int)
    y_ := y.(int)
    z_ := z.(int)
    return (x_ + y_ == z_) || (x_ + z_ == y_) || (y_ + z_ == x_)
}



