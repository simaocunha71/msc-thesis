    runes := []rune(s)
    newRunes := make([]rune, 0)
    for _, ch := range runes {
        newRunes = append(newRunes, (ch-5-'a')%26+'a')
    }
    return string(newRunes)
}

It seems like you're trying to shift every character in the input string by 5 places in the alphabet, but there's a mistake in your EncodeShift function. The line (ch+5-'a')%26+'a' should actually be (ch-5-'a')%26+'a' to shift characters 5 places to the right. 

Also, the DecodeShift function is not returning the correct results because it's using the wrong formula to shift characters. It should be (ch+5-'a')%26+'a' to shift characters 5 places to the left. 

I've corrected these issues in the functions below:

EncodeShift:

func EncodeShift(s string) string {
    runes := []rune(s)
    newRunes := make([]rune, 0)
    for _, ch := range runes {
        newRunes = append(newRunes, (ch-5-'a')%26+'a')
    }
    return string(newRunes)
}

DecodeShift:

func DecodeShift(s string) string {
    runes := []rune(s)
    newRunes := make([]rune, 0)
    for _, ch := range runes {
        newRunes = append(newRunes, (ch+5-'a')%26+'a')
    }
    return string(