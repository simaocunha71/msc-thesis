    strToNum := map[string]string{
        "zero" : "0", "one" : "1", "two" : "2", "three" : "3", "four" : "4",
        "five" : "5", "six" : "6", "seven" : "7", "eight" : "8", "nine" : "9",
    }

    numToStr := map[string]string{
        "0" : "zero", "1" : "one", "2" : "two", "3" : "three", "4" : "four",
        "5" : "five", "6" : "six", "7" : "seven", "8" : "eight", "9" : "nine",
    }

    nums := strings.Split(numbers, " ")
    for i, num := range nums {
        nums[i] = strToNum[num]
    }

    sort.Strings(nums)

    for i, num := range nums {
        nums[i] = numToStr[num]
    }

    return strings.Join(nums, " ")
}



