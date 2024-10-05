    str = strings.ToLower(str)
    return len(strings.ReplaceAll(str, "", ""))
}  // strings.ReplaceAll(str, "", "") is used to remove all spaces from the string, then the length of the string is the number of distinct characters.