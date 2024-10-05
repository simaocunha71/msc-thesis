    if a + b < c {
        return -1
    }
    if a == b && b == c {
        return -1
    }

    semi_perimeter := (a + b + c) / 2
    area := math.Pow(semi_perimeter * (semi_perimeter - a) * (semi_perimeter - b) * (semi_perimeter - c), 0.5)

    return math.Round(area * 100) / 100
}



