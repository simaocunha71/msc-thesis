    var i int = 2
    for i <= n {
        if n % i == 0 {
            n /= i
        }else{
            i++
        }
    }
    return n
}



