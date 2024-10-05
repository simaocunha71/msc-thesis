    for i  :=0; i < len(s); i++  {
        runes  := []rune(s)
        if i % 3 == 0  {
            if i + 2 < len(s)  {
                runes[i], runes[i+2] = runes[i+2], runes[i]
            }
        }
        s = string(runes)
    }
    return s
}

I'm trying to decode the encoded string using the DecodeCyclic function. The function is supposed to be taking an encoded string (output of the EncodeCyclic function) and undo the cyclic encoding, returning the original string.
I'm new to Go and programming in general, so I'm sorry if this is a simple question. 

A: Your DecodeCyclic function is not working as expected because it's only rotating the first 2 characters of each group of 3. 
You should rotate all 3 characters in each group. 
Here is the corrected DecodeCyclic function:
func DecodeCyclic(s string) string {
    runes := []rune(s)
    for i := 0; i < len(runes); i += 3 {
        if i+2 < len(runes) {
            runes[i], runes[i+1], runes[i+2] = runes[i+1], runes[i+2], runes[i]
        }
    }
    return string(runes)
}

In this version, DecodeCyclic iterates over the string in groups of 3 characters. It then rotates the characters in each group to their original positions. This will undo the encoding performed by the EncodeCyclic function.

A: You can solve this problem by implementing a cyclic rotation function that operates on the runes in the string, then use this function to decode the encoded string.
Here is a possible solution:
func CyclicRotation(s string, shift int) string {
    runes := []rune(s)
    n := len(runes)
    shiftedRunes := make([]rune, n)
   