
// This function takes two positive numbers x and y and returns the
// biggest even integer number that is in the range [x, y] inclusive. If
// there's no such number, then the function should return -1.
// 
// For example:
// ChooseNum(12, 15) = 14
// ChooseNum(13, 12) = -1
func ChooseNum(x, y int) int {
    if x == y {
        return x
    } else if y < (x-1)/2+1{
        return ChooseNum(-y+(x-1)/2, x)
    } else {
        return ChooseNum((x-1)/2 + 1 , -y)
    }
}
