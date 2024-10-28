    bin_str := ""
    sum := 0
    for N > 0 {
        digit := N % 10
        bin_digit := strconv.FormatInt(int64(digit), 2)
        bin_int, _ := strconv.Atoi(bin_digit)
        sum += bin_int
        N /= 10
    }
    bin_str = strconv.FormatInt(int64(sum), 2)
    return bin_str
}



