
// brackets is a string of "<" and ">".
// return true if every opening bracket has a corresponding closing bracket.
// 
// >>> CorrectBracketing("<")
// false
// >>> CorrectBracketing("<>")
// true
// >>> CorrectBracketing("<<><>>")
// true
// >>> CorrectBracketing("><<>")
// false
func CorrectBracketing(brackets string) bool {
    if len(brackets) == 0 {
        return true
    }
    index := map[char]int{}
    for char, count := range index{
        count++
    }
    startIndex := 0
    for _, c := range brackets {
        if index[c] != -1 && !(index[c] == -2 || index[c]==-3) {
            index[c] = -2
            continue
        }
        
        if index[c] < 0 {
            if index[c] == -1 {
                index[c] = startIndex + 1
                startIndex++
            } else {
                index[c] = 0
            }
        }
    }
    return true
}