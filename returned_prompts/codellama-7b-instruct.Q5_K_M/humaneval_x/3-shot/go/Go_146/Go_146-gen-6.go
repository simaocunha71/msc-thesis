    var result int = 0

    for i := 0; i < len(nums); i++ {
        if nums[i] > 10 {
            if strconv.Itoa(nums[i])[0] == "1" || strconv.Itoa(nums[i])[0] == "3" || strconv.Itoa(nums[i])[0] == "5" || strconv.Itoa(nums[i])[0] == "7" || strconv.Itoa(nums[i])[0] == "9" {
                if strconv.Itoa(nums[i])[len(strconv.Itoa(nums[i])) - 1] == "1" || strconv.Itoa(nums[i])[len(strconv.Itoa(nums[i])) - 1] == "3" || strconv.Itoa(nums[i])[len(strconv.Itoa(nums[i])) - 1] == "5" || strconv.Itoa(nums[i])[len(strconv.Itoa(nums[i])) - 1] == "7" || strconv.Itoa(nums[i])[len(strconv.Itoa(nums[i])) - 1] == "9" {
                    result += 1
                }
            }
        }
    }
    return result
}



