    re := regexp.MustCompile("[aeiouAEIOU]")
    text = re.ReplaceAllString(text, "")
    return text
}

func main() {
    fmt.Println(RemoveVowels(""))
    fmt