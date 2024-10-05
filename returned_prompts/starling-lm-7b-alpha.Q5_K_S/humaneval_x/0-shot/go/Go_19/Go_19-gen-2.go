    var nums []string
    for _, v := range strings.Fields(numbers) {
        switch v {
        case "zero":
            nums = append(nums, "0")
        case "one":
            nums = append(nums, "1")
        case "two":
            nums = append(nums, "2")
        case "three":
            nums = append(nums, "3")
        case "four":
            nums = append(nums, "4")
        case "five":
            nums = append(nums, "5")
        case "six":
            nums = append(nums, "6")
        case "seven":
            nums = append(nums, "7")
        case "eight":
            nums = append(nums, "8")
        case "nine":
            nums = append(nums, "9")
        }
    }

    sort.Strings(nums)

    var result []string
    for _, v := range nums {
        switch v {
        case "0":
            result = append(result, "zero")
        case "1":
            result = append(result, "one")
        case "2":
            result = append(result, "two")
        case "3":
            result = append(result, "three")
        case "4":
            result = append(result, "four")
        case "5":
            result = append(result, "five")
        case "6":
            result = append(result, "six")
        case "7":
            result = append(result, "seven")
        case "8":
            result = append(result, "eight")
        case "9":
            result = append(result, "nine")
        }
    }

    return strings.Join(result, " ")
}

































































