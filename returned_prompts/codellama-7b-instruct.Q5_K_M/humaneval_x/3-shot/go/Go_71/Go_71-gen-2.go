    if a+b>c && b+c>a && a+c>b{
        return math.Round(math.Sqrt(float64(a*a+b*b+c*c))/2)
    }else{
        return -1
    }
}



