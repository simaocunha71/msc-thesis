    if a + b > c && a + c > b && b + c > a{
        return math.Round(math.Sqrt(math.Pow(a,2) + math.Pow(b,2) + math.Pow(c,2))/2 * 100) / 100
    }else{
        return -1
    }
}



