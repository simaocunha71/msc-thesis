    var max_prime_num int = 0
    var prime_sum int = 0
    var num_digits int = 0
    var num_digits_str string = ""
    var prime_digits_sum int = 0
    var temp_sum int = 0

    for _, num := range lst{
        prime_sum = 0
        num_digits = 0
        num_digits_str = strconv.Itoa(num)
        for _, digit := range num_digits_str{
            prime_sum += int(digit-'0')
            num_digits += 1
        }

        for _, digit := range num_digits_str{
            temp_sum += int(digit-'0')
        }

        if temp_sum == prime_sum && temp_sum > max_prime_num{
            max_prime_num = temp_sum
        }
    }

    return max_prime_num
}



