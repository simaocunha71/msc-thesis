    if len(arr) == 0{
        return nil
    }

    var result int
    var product int
    var sign int

    for _, c := range arr {
        sign = 1
        if c < 0{
            sign = -1
        }
        result += math.Abs(c)
        product *= sign
    }

    return product * result
}



