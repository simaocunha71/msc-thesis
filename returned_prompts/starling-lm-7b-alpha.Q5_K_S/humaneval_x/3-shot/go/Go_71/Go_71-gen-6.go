    perimeter := (a + b + c)/2
    if perimeter < a || perimeter < b || perimeter < c {
        return -1
    }
    area := math.Sqrt(perimeter * (perimeter - a) * (perimeter - b) * (perimeter - c))
    return math.Round(area*100)/100
}



