    if x==1{
        return true
    }
    var result float64= math.Pow(float64(x), 1/float64(n))
    return result == float64(int(result))
}



