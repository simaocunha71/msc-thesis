func HexKey(num string) int {
    count := 0
    for _, v := range num {
        switch v {
        case '2', '3', '5', '7':
            count++
        case 'A', 'B', 'D', 'E':
            count++
        case 'B':
            count++
        case 'D':
            count++
        }
    }
    return count
}