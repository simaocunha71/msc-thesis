    if len(arr)==0{
        return nil
    }

    sum_magnitudes := 0
    prod_signs := 1

    for _,v := range arr{
        sum_magnitudes += int(math.Abs(float64(v)))
        if v<0{
            prod_signs *= -1
        }else if v>0{
            prod_signs *= 1
        }else{
            return 0
        }
    }

    return prod_signs*sum_magnitudes
}



