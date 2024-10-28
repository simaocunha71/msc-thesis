    if a+b > c && b+c > a && a+c > b{
        semi_perimeter := (a+b+c)/2
        return math.Round(math.Sqrt(semi_perimeter * (semi_perimeter - a) * (semi_perimeter - b) * (semi_perimeter - c)),2)
    }
    return -1
}




