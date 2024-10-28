    binary_str := make([]byte, 0)
    binary_str = append(binary_str, '1')
    binary_sum := 1
    for ; N > 0; N /= 2 {
        binary_sum += N % 2
        binary_str = append(binary_str, '0')
    }
    return strconv.FormatInt(int64(binary_sum), 2)
}



