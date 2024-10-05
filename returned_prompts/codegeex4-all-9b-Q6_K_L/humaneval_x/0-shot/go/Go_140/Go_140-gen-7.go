func FixSpaces(text string) string {
    text = strings.ReplaceAll(text, " ", "_")
    text = strings.ReplaceAll(text, "___", "-")
    text = strings.ReplaceAll(text, "__", "-")
    return text
}