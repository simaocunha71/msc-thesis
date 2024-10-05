    var result []int
    for i := 0; i < len(nums); i++ {
        var temp string = strconv.Itoa(nums[i])
        var sum int = 0
        for _, c := range temp {
            sum += int(c - '0')
        }
        result = append(result, sum)
    }
    sort.Ints(result)

    return result
}



