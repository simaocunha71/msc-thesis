    num, _ := strconv.ParseFloat(value, 64)
    int_part := int(math.Round(num))
    if int_part == num {
        return int_part
    }
    str_int_part := strconv.Itoa(int_part)
    str_num := strings.Replace(value, str_int_part, "", 1)
    int_str_num, _ := strconv.Atoi(str_num)

    if int_str_num >= 5 {
        return int_part + 1
    }
    return int_part
}



