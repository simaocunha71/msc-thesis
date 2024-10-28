    return strings.Split(s, " ")
}

// Alternatively, you could use strings.Split(s, ", ") to split by both commas and spaces. However, this will not work correctly if the input string contains spaces within quotes (like "hello, world"). In that case, you would need a more complex solution that parses the string based on the rules of the language.