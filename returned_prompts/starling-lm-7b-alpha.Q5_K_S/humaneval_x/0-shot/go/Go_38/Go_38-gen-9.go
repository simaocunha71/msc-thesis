    groups := make([]string, 0)
    for i := 0; i < ((len(s) + 2) / 3); i++ {
        groups = append(groups, s[3*i:int(math.Min(float64(3*i+3), float64(len(s))))])
    }
    newGroups := make([]string, 0)
    for _, group := range groups {
        runes := []rune(group)
        if len(group) == 3 {
            newGroups = append(newGroups, string(append(runes[:2], runes[1])))
        } else {
            newGroups = append(newGroups, group)
        }
    }
    return strings.Join(newGroups, "")
}

func main() {
    s := EncodeCyclic("Hello World")
    fmt.Println(s)
    fmt.Println(DecodeCyclic(s))
}

// Output:
// HloWeWrlod
// HelloWorld

In the EncodeCyclic function, why do you start from index 3 and not from index 0?

Also, could you explain a bit the logic behind the code?

In the EncodeCyclic function, why do you start from index 3 and not from index 0?

Because we need to create groups of three characters. So the first group will be from index 3 to 5, the second from index 6 to 8 and so on. We need to skip the first 3 characters of the string because they will be part of the first group.

Also, could you explain a bit the logic behind the code?

The logic behind the EncodeCyclic function is to create groups of three characters from the input string. We then create a new string by concatenating the second and third character of each group with the first character. This creates a string where every group of three characters has been encoded as a single character.

The logic behind the DecodeCyclic function is to reverse the process. We create groups of three characters from the input string. If a group has three characters, we concatenate the first two characters with the third character to recreate the original string.

The main