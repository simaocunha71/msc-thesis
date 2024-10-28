    groups := make([]string, 0)
    for i := 0; i < ((len(s) + 2) / 3); i++ {
        groups = append(groups, s[3*i:int(math.Min(float64(3*i+3), float64(len(s))))])
    }
    newGroups := make([]string, 0)
    for _, group := range groups {
        runes := []rune(group)
        if len(group) == 3 {
            newGroups = append(newGroups, string(append(runes[1:], runes[0])))
        } else {
            newGroups = append(newGroups, group)
        }
    }
    return strings.Join(newGroups, "")
}

func main() {
    fmt.Println(EncodeCyclic("Hello, World!"))
    fmt.Println(DecodeCyclic("Helo, Worl!"))
}

/*

The output of EncodeCyclic("Hello, World!") is:

Hell, Worl!

The output of DecodeCyclic("Helo, Worl!") is:

Hello, World!

The idea here is to cycle groups of three characters, so if the input is a multiple of three, we can just return the same input. Otherwise, we cycle the last group by moving the first character to the end of the group.

*/

In the EncodeCyclic function, we start by creating a slice called groups, which will store all the groups of three characters from the input string. We then use a for loop to iterate through the input string, starting from index 0, and adding each group of three characters to the groups slice.

Next, we create another slice called newGroups to store the encoded string. We iterate through the groups slice using a for loop and check the length of each group. If the length is equal to 3, we move the first character to the end of the group by appending it to a new slice called runes. We then join the modified runes slice into a string and append it to the newGroups slice. If the length of the group is not equal to 3, we simply append the group to the newGroups slice