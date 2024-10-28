    count := 0

    for _, num := range nums {
        if num > 10 {
            first_digit := strconv.Itoa(num)[0]
            last_digit := strconv.Itoa(num)[len(strconv.Itoa(num))-1]

            if first_digit == "1" || first_digit == "3" || first_digit == "5" || first_digit == "7" || first_digit == "9" {
                if last_digit == "1" || last_digit == "3" || last_digit == "5" || last_digit == "7" || last_digit == "9" {
                    count++
                }
            }
        }
    }
    return count
}

