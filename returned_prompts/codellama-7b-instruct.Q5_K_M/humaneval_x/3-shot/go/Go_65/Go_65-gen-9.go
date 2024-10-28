    var result string
    str_x := strconv.Itoa(x)
    if shift>len(str_x){
        result = str_x
    }else{
        result = str_x[shift:]+str_x[:shift]
    }
    return result
}



