    var nums []string
    for _, n := range strings.Split(numbers, " ") {
        if n != "" {
            nums = append(nums, n)
        }
    }
    sort.Strings(nums)
    return strings.Join(nums, " ")
}

