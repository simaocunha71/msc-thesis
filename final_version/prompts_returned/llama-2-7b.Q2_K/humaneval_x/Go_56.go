
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
    
    for openingBracket := range brackets {
        count := 1
        for nextOpeningBracketIndex, nextOpeningBracket := range brackets {
            switch nextOpeningBracket {
                case '>':
                    if openingBracket == '<' && nextOpeningBracket == '>' {
                        continue
                    } else if count > 0 {
                        return false
                    }
                    
                    count += 1
                default:
                    if count == 0 { // ignore this opening bracket
                        continue
                    }
            }
            
            count -= 1
        }
    }
    
    return true
}
