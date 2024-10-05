    x_numerator, x_denominator, x_err := strconv.Atoi(strings.Split(x, "/")[0])
    n_numerator, n_denominator, n_err := strconv.Atoi(strings.Split(n, "/")[0])
    if x_err != nil || n_err != nil{
        return false
    }

    var gcd int = 1
    for i:=1; i <= x_denominator; i++ {
        if x_denominator % i == 0 && n_denominator % i == 0{
            gcd = i
        }
    }

    x_denominator = x_denominator / gcd
    n_denominator = n_denominator / gcd

    if x_numerator * n_denominator == x_denominator * n_numerator{
        return true
    }else{
        return false
    }
}



