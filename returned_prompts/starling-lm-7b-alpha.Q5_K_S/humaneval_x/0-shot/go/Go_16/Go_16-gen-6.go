    count := 0
    distinctCharacters := make(map[rune]bool)

    for _, char := range str {
        if !distinctCharacters[tolower(char)] {
            count++
            distinctCharacters[tolower(char)] = true
        }
    }
    return count
}

func tolower(char rune) rune {
    if char >= 'A' && char <= 'Z' {
        return char + 'a' - 'A'
    }
    return char
}

func main() {
    fmt.Println(CountDistinctCharacters("xyzXYZ"))
    fmt.Println(CountDistinctCharacters("Jerry"))
}


















In the code above, the CountDistinctCharacters function takes a string as input and returns the number of distinct characters in the string. The function uses a map called "distinctCharacters" to keep track of whether a character has already been encountered. It iterates over each character in the string and checks if the lowercase version of the character is already in the map. If it is not, it increments the count and adds the lowercase character to the map.

The tolower function is a helper function that converts uppercase characters to lowercase. It is used in the CountDistinctCharacters function to ensure that the comparison between characters is case-insensitive.

In the main function, the CountDistinctCharacters function is called with two different strings as arguments, and the results are printed to the console.

The output of the code is:
3
4
This means that the first string, "xyzXYZ", consists of 3 distinct characters, and the second string, "Jerry", consists of 4 distinct characters.








































































































