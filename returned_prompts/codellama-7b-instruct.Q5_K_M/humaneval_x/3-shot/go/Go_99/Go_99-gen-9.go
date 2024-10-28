    number, _ := strconv.ParseFloat(value, 64)
    rounded_number := math.Round(number)
    rounded_number_str := strconv.Itoa(int(rounded_number))
    if rounded_number == math.Trunc(number) {
        return int(rounded_number)
    } else if rounded_number_str[0] == "-" {
        return int(rounded_number) - 1
    } else {
        return int(rounded_number) + 1
    }
}



