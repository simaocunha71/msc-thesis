    var even, odd int
    for i := 0; i < len(strconv.Itoa(num)); i++ {
        if (strconv.Itoa(num)[i] == '0' || strconv.Itoa(num)[i] == '2' || strconv.Itoa(num)[i] == '4' || strconv.Itoa(num)[i] == '6' || strconv.Itoa(num)[i] == '8') && (strconv.Itoa(num)[i] != '0') {
            even += 1
        }

        if (strconv.Itoa(num)[i] == '1' || strconv.Itoa(num)[i] == '3' || strconv.Itoa(num)[i] == '5' || strconv.Itoa(num)[i] == '7' || strconv.Itoa(num)[i] == '9') && (strconv.Itoa(num)[i] != '0') {
            odd += 1
        }
    }
    return [2]int{even, odd}
}



