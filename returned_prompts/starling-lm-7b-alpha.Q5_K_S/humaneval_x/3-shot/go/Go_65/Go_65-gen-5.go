    var digits_str_arr []string
    var result_str string

    for {
        div := x / 10
        rem := x % 10
        digits_str_arr = append(digits_str_arr,string(rune(rem + '0')))
        x = div
        if x == 0 {
            break
        }
    }

    shift %= len(digits_str_arr)

    for i:= 0; i < len(digits_str_arr); i++ {
        if shift > 0 {
            shift -= 1
            continue
        }

        result_str += digits_str_arr[i]
    }

    return result_str
}



