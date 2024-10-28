    var t = make([]float64, n+1)
    if n>=0 {
        t[0] = 3
    }
    if n>=1 {
        t[1] = 3
    }
    if n>=2 {
        t[2] = 2
    }
    for i := 3; i <= n; i++ {
        if i%2 == 0 {
            t[i] = 1 + float64(i)/2
        } else {
            t[i] = t[i-1] + t[i-2] + t[i+1]
        }
    }
    return t
}



