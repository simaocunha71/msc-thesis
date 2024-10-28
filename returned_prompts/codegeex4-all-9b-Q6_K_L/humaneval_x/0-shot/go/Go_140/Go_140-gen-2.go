func FixSpaces(text string) string {
    text = strings.ReplaceAll(text, " ", "_")
    text = strings.ReplaceAll(text, "__", "-")
    text = strings.ReplaceAll(text, "_-", "-")
    text = strings.ReplaceAll(text, "-_", "-")
    return text
}