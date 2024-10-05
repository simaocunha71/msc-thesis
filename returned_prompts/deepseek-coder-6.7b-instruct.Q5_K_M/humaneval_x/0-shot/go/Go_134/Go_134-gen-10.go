    if len(txt)==0 {
        return false
    }
    if len(txt)==1 {
        return txt[0]>='a' && txt[0]<='z' || txt[0]>='A' && txt[0]<='Z'
    }
    if txt[len(txt)-1]>='a' && txt[len(txt)-1]<='z' || txt[len(txt)-1]>='A' && txt[len(txt)-1]<='Z' {
        return !strings.ContainsAny(txt[len(txt)-2:len(txt)-1], " ")
    }
    return false
}

func main() {
    fmt.Println(CheckIfLastCharIsALetter("apple pie"))  // ➞ false
    fmt.Println(CheckIfLastCharIsALetter("apple pi e")) // ➞ true
    fmt.Println(CheckIfLastCharIsALetter("apple pi e ")) // ➞ false
    fmt.Println(CheckIfLastCharIsALetter("")) // ➞ false
}

This code checks if the last character of the string is a letter. If it is, it checks if it's not part of a word (i.e., it's not preceded or followed by a space). If both conditions are met, the function returns true; otherwise, it returns false.
*/

func CheckIfLastCharIsALetter(txt string) bool {
	if len(txt) == 0 || (txt[len(txt)-1] < 'A' || (txt[len(txt)-1] > 'Z' && txt[len(txt)-1] < 'a') || txt[len(txt)-1] > 'z') {
		return false
	}
	if len(txt) == 1 {
		return true
	}
	return txt[len(txt)-2] == ' ' || txt[len(txt)-1] == ' '
}

func main() {
	fmt.Println(CheckIfLastCharIsALetter("apple pie"))  // ➞ false
	fmt.Println(CheckIfLastCharIsALetter