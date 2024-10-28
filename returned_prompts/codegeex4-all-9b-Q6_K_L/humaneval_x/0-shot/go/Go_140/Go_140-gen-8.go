func FixSpaces(text string) string {
    // Replace all spaces with underscores
    text = strings.ReplaceAll(text, " ", "_")
    
    // Replace all consecutive underscores with a single underscore
    text = strings.ReplaceAll(text, "__", "_")
    
    // Replace all consecutive underscores with a single dash
    text = strings.ReplaceAll(text, "__", "-")
    
    return text
}

This solution uses the `strings.ReplaceAll` function to replace all occurrences of a string in the text. The first replacement replaces all spaces with underscores, and the next two replacements replace all consecutive underscores with a single underscore and a dash, respectively.

Note that the order of replacements is important. We first replace all spaces with underscores, then replace all consecutive underscores with a single underscore, and finally replace all consecutive underscores with a single dash. This ensures that we get the desired output.

The time complexity of this solution is O(n), where n is the length of the input string. This is because we need to iterate over the string once for each replacement operation. The space complexity is also O(n), as we need to create a new string for each replacement operation.