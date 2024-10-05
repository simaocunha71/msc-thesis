    fibNum := 0
    a, b := 1, 1
    count := 0

    for {
        fibNum = a
        a, b = b, a+b
        if math.Mod(float64(fibNum), 2.0) == 1.0 {
            count++
            if count == n {
                return fibNum
            }
        }
    }
}
}  // end of package main



