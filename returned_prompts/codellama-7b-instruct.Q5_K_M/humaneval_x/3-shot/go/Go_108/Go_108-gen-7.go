    result := 0
    for _, num := range arr{
        var signed_digits []int
        var sum int

        if num < 0{
            signed_digits = []int{num}
            for i:=1; i<len(strconv.Itoa(num)); i++{
                signed_digits = append(signed_digits, int(math.Abs(float64(num))%10))
                num /= 10
            }
        }else{
            signed_digits = []int{num}
            for i:=1; i<len(strconv.Itoa(num)); i++{
                signed_digits = append(signed_digits, int(math.Abs(float64(num))%10))
                num /= 10
            }
        }

        for _, digit := range signed_digits{
            sum += digit
        }
        if sum > 0{
            result += 1
        }
    }
    return result
}



