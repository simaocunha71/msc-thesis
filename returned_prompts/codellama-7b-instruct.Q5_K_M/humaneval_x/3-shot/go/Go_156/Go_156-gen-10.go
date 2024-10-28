    var result []string
    ones := []string{"", "i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix"}
    tens := []string{"", "x", "xx", "xxx", "xl", "l", "lx", "lxx", "lxxx", "xc"}
    hundreds := []string{"", "c", "cc", "ccc", "cd", "d", "dc", "dcc", "dccc", "cm"}
    thousands := []string{"", "m", "mm", "mmm", "m", "mm", "mmm", "mmm", "mmm", "mmm"}

    num_ones := number % 10
    number /= 10
    num_tens := number % 10
    number /= 10
    num_hundreds := number % 10
    number /= 10
    num_thousands := number

    result = append(result, thousands[num_thousands])
    result = append(result, hundreds[num_hundreds])
    result = append(result, tens[num_tens])
    result = append(result, ones[num_ones])

    return strings.Join(result, "")
}



