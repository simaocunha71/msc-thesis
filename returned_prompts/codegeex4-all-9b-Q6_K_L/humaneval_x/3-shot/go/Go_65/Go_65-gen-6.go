    x_string := strconv.Itoa(x)
    n := len(x_string)

    if shift > n{
        return ReverseString(x_string)
    }else{
        return x_string[shift:] + x_string[:shift]
    }
}



