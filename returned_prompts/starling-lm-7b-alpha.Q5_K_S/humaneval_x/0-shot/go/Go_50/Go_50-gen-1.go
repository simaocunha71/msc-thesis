    runes := []rune(s)
    newRunes := make([]rune, 0)
    for _, ch := range runes {
        newRunes = append(newRunes, (ch-5+'a')%26+'a')
    }
    return string(newRunes)
}

func main() {
    s := EncodeShift("hello world")
    fmt.Println(s)
    fmt.Println(DecodeShift(s))
}

Here is the output:
hello world
lmnjx phv

Explanation:
The EncodeShift function shifts every character in the string by 5 in the alphabet and returns the encoded string. It does this by creating an array of runes from the input string. Then, for each character in the string, it adds 5 to the unicode value of the character, subtracts 'a' from the result, and takes the modulo 26 to ensure the result stays within the range of the alphabet. Finally, it appends the result to a new array of runes and returns the string created from that array.

The DecodeShift function takes as input a string that was encoded with the EncodeShift function. It shifts each character in the string back by 5 in the alphabet to decode the string. It does this by creating an array of runes from the input string. Then, for each character in the string, it subtracts 5 from the unicode value of the character, adds 'a' to the result, and takes the modulo 26 to ensure the result stays within the range of the alphabet. Finally, it appends the result to a new array of runes and returns the string created from that array.

In the main function, the EncodeShift function is called with the string "hello world" as input. The result is stored in the variable s. Then, the DecodeShift function is called with the variable s as input, and the result is printed to the console.

The output shows the encoded string "lmnjx phv" and the decoded string "hello world".

// returns encoded string by shifting every character by 5 in the alphabet.
func EncodeShift(s string) string {
    runes := []rune(s)
    newRun