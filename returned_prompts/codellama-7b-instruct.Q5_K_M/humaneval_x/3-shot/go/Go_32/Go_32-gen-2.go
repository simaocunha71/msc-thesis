    if len(xs) % 2 == 1 {
        panic("Odd number of coefficients")
    }
    var n int = len(xs) / 2
    var x_lo float64 = 0
    var x_hi float64 = 1
    for i := 0; i < 100; i++ {
        x_mid := (x_lo + x_hi) / 2
        y_mid := Poly(xs, x_mid)
        if y_mid == 0 {
            return x_mid
        }
        if math.Abs(y_mid) < 1e-8 {
            return x_mid
        }
        if y_mid > 0 {
            x_lo = x_mid
        } else {
            x_hi = x_mid
        }
    }
    return -1
}
