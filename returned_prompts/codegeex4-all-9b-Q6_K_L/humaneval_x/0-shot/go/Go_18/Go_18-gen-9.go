func HowManyTimes(str string, substring string) int {
    var count int
    for i := 0; i <= len(str)-len(substring); i++ {
        if str[i:i+len(substring)] == substring {
            count++
        }
    }
    return count
}