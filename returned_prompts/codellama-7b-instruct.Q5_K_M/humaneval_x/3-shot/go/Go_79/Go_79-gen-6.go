    binary_string := make([]byte, 0)
    binary_string = append(binary_string, "db"...)
    for i := 0; i < 16; i++ {
        if decimal&(1<<uint(15-i)) != 0 {
            binary_string = append(binary_string, "1")
        }else {
            binary_string = append(binary_string, "0")
        }
    }
    binary_string = append(binary_string, "db"...)
    return string(binary_string)
}



