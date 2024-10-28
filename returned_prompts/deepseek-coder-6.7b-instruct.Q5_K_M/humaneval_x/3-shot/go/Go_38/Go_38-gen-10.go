    groups  := make([]string, 0)
    for i  := 0; i < ((len(s) +2) / 3); i++  {
        groups  = append(groups, s[3*i:int(math.Min(float64(3*i+3), float64(len(s))))])
     }
    newGroups  := make([]string, 0)
    for  _, group  := range groups  {
        runes  := []rune(group)
        if len(group) == 3  {
            newGroups  = append(newGroups, string(append([]rune{runes[len(runes)-1]}, runes[0:len(runes)-1]...)))
        } else  {
            newGroups  = append(newGroups, group)
        }
    }
    return strings.Join(newGroups, "")
}

// Function to create a "rotated" string. It should take as input a string and an amount by which to rotate the characters
// in the string. Rotation is to be performed in a cyclic manner.
// 
// If the rotation amount is positive, rotation is to the right; if it's negative, rotation is to the left.
// 
// The function returns the rotated string.
// 
// 
// For example, if we have the string "ABCDE" and we want to rotate it 2 positions to the right, the result is "DEABC".
// If we rotate it 2 positions to the left, we get "CDEAB".
// 
// 
// Hint: You may want to use the modulus operator (%) to wrap around to the start of the string when rotating to the right.
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
//