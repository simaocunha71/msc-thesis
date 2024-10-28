
// Given a non-empty list of integers lst. Add the even elements that are at odd indices..
// 
// Examples:
// Add([4, 2, 6, 7]) ==> 2
func Add(lst []int) int {
    sum := 0
    for i := 0; i < len(lst); i++ {
        if i%2 == 0 && lst[i]%2 == 0 {
            sum += lst[i]
        }
    }
    return sum
}
