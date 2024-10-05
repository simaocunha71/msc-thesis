    var sum int
    for _, num := range lst {
        if num > 0 && math.Mod(num, 2) == 1 {
            sum += int(num * num)
        }
    }
    return sum
}  // the time complexity is O(n) where n is the length of the input list. The space complexity is O(1) as no extra space is used.