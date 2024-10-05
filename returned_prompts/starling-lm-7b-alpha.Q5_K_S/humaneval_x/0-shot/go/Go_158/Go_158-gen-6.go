    type CharacterCounter struct {
        C []rune
        L int
    }

    var maxCharacters int
    var maxCharacter string

    for _, word := range words {
        cc := CharacterCounter{C: make([]rune, 26), L: 0}

        for _, c := range word {
            if c >= 'a' && c <= 'z' {
                cc.C[c-'a']++
                cc.L++
            }
        }

        if cc.L > maxCharacters {
            maxCharacters = cc.L
            maxCharacter = word
        } else if cc.L == maxCharacters {
            if string(word) < maxCharacter {
                maxCharacter = word
            }
        }
    }

    return maxCharacter
}

Here's a detailed explanation of the algorithm:

1. Iterate over the input array of strings, and for each string do the following:

    a. Create a CharacterCounter struct, which holds the number of unique characters in the string, along with an array of length 26 (to accommodate ASCII characters) to keep track of the frequency of each character.

    b. For each character in the string, if it's a lowercase alphabetic character, increment the corresponding index of the frequency array in CharacterCounter struct and update the count of unique characters.

    c. After iterating over all characters in the string, compare the count of unique characters in the current string with the maximum count found so far. If the count is higher, update the maximum count and the maximum character. If the count is the same as the maximum count, update the maximum character if the current string is lexicographically smaller.

2. After iterating over all the strings, return the maximum character.

Here's an example usage of the FindMax function:

func main() {
    words := []string{"name", "of", "string"}
    result := FindMax(words)
    fmt.Println(result) // Output: "string"
}

The output of the above code will be "string" because the string "string" has the maximum number of unique characters among all the strings in the input array.

The time complexity of