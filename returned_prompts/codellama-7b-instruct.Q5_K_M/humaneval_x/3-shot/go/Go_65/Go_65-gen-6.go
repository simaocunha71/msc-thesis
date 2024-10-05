    str_x := IntToStr(x)
    str_x_len := len(str_x)
    if shift > str_x_len{
        shift = str_x_len
    }
    var str_result string = ""
    for i:=shift; i<str_x_len; i++ {
        str_result += string(str_x[i])
    }
    for i:=0; i<shift; i++ {
        str_result += string(str_x[i])
    }
    return str_result
}



