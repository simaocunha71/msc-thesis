    if len(arr) == 0 {
        return nil
    }

    var sum int
    var product int

    for i, v := range arr {
        if i == 0 {
            sum += math.Abs(int64(v))
            product = v
        } else {
            sum += math.Abs(int64(v))
            product *= v
        }
    }

    if product < 0 {
        return sum * -1
    } else {
        return sum
    }
}



