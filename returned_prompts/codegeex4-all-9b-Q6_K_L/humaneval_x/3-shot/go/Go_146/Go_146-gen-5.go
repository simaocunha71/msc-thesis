    count := 0
    for i := 0; i < len(nums); i++ {
        if nums[i] > 10 {
            first_digit := strconv.Itoa(nums[i])[0]
            last_digit := strconv.Itoa(nums[i])[len(strconv.Itoa(nums[i]))-1]
            if first_digit == '1' || first_digit == '3' || first_digit == '5' || first_digit == '7' || first_digit == '9' {
                if last_digit == '1' || last_digit == '3' || last_digit == '5' || last_digit == '7' || last_digit == '9' {
                    count += 1
                }
            }
        }
    }
    return count
}



