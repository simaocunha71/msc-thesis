    var sum int = 0
    for i := 1; i < math.Pow(10, float64(n)); i++ {
        var str string = string(i)
        if str[0] == '1' || str[len(str)-1] == '1' {
            sum += 1
        }
    }
    return sum
}



