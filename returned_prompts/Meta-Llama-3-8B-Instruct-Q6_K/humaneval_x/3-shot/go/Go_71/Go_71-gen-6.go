    var result float64
    var flag bool
    if a+b>c && a+c>b && b+c>a {
        p := (a+b+c) / 2
        result = math.Sqrt(p*(p-a)*(p-b)*(p-c))
        flag = true
    }else{
        flag = false
    }
    if flag {
        return float64(math.Round(float64(result*10000.0))/10000.0)
    }else{
        return -1
    }
}