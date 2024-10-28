    num, _ := strconv.ParseFloat(value, 64)
    int_part := int(math.Floor(num))

    if math.Abs(num - int_part) == math.Abs(int_part + 1 - num) {
        return int_part + 1
    }else if math.Abs(num - int_part) == math.Abs(int_part - 1 - num) {
        return int_part - 1
    }else {
        return int_part
    }
}



