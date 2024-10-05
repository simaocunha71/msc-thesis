    if len(arr)==0 {
        return nil
    }

    var result int
    var prod_sign int
    var abs_arr []int
    var abs_arr_sum int

    for _, num := range arr {
        abs_arr = append(abs_arr, math.Abs(num))
    }

    for _, num := range abs_arr {
        abs_arr_sum += num
    }

    for _, num := range arr {
        if num != 0 {
            prod_sign = 1
            if num < 0 {
                prod_sign = -1
            }
            result += prod_sign * num
        }
    }

    return abs_arr_sum * result
}



