    x_int := int(x.(float64))
    y_int := int(y.(float64))
    z_int := int(z.(float64))

    return (x_int == y_int + z_int) || (y_int == x_int + z_int) || (z_int == y_int + x_int)
}

