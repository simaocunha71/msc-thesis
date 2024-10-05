    if len(txt) == 0 {
        return false
    }

B:
    if txt[len(txt)-1] >= 'a' && txt[len(txt)-1] <= 'z' || txt[len(txt)-1] >= 'A' && txt[len(txt)-1] <= 'Z' {
        C:
        for i := len(txt) - 2; i >= 0; i-- {
            if txt[i] == ' ' {
                return txt[i+1] != txt[len(txt)-1]
            }
        }
        return true
    }

    return false
}

func main() {
    fmt.Println(CheckIfLastCharIsALetter("apple pie")) //➞ false
    fmt.Println(CheckIfLastCharIsALetter("apple pi e")) //➞ true
    fmt.Println(CheckIfLastCharIsALetter("apple pi e ")) //➞ false
    fmt.Println(CheckIfLastCharIsALetter("")) //➞ false
}

*/

func CheckIfLastCharIsALetter(txt string) bool {

	if len(txt) == 0 {
		return false
	}

	lastChar := txt[len(txt)-1]
	if (lastChar >= 'a' && lastChar <= 'z') || (lastChar >= 'A' && lastChar <= 'Z') {
		for i := len(txt) - 2; i >= 0; i-- {
			if txt[i] == ' ' {
				return txt[i+1] != lastChar
			}
		}
		return true
	}

	return false
}

func main() {
	fmt.Println(CheckIfLastCharIsALetter("apple pie"))      //➞ false
	fmt.Println(CheckIfLastCharIsALetter("apple pi e"))      //➞ true
	fmt.Println(CheckIfLastCharIsALetter("apple pi e "))     //➞ false
	fmt.Println(CheckIfLastCharIsALetter(""))                //➞ false
	fmt.