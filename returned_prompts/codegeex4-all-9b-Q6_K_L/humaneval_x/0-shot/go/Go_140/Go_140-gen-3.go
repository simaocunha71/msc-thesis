func FixSpaces(text string) string {
    text = strings.Replace(text, " ", "_", -1)
    text = strings.Replace(text, "__", "-", -1)
    text = strings.Replace(text, "---", "-", -1)
    text = strings.Replace(text, "___", "-", -1)
    return text
}