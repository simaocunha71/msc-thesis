    if len(xs)%2 == 1{
        panic("xs must have even number of elements")
    }
    var max_abs_coeff float64 = 0
    for i, v := range xs {
        if i % 2 == 0{
            continue
        }
        if abs(v) > max_abs_coeff{
            max_abs_coeff = abs(v)
        }
    }
    if max_abs_coeff == 0{
        return 0
    }
    var min_x float64 = 0
    var max_x float64 = 1
    var mid_x float64
    var mid_value float64
    var last_mid_value float64
    for {
        mid_x = (min_x + max_x) / 2
        mid_value = Poly(xs, mid_x)
        if abs(mid_value) < max_abs_coeff{
            return mid_x
        }
        if mid_value * last_mid_value > 0{
            min_x = mid_x
        }else{
            max_x = mid_x
        }
        last_mid_value = mid_value
    }
    return 0
}



