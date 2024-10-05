func IsBored(S string) int {
    var boredoms int
    re := regexp.MustCompile(`(?i)(^i)\b`)
    for _, sentence := range regexp.MustCompile(`[.?!]\s`).Split(S, -1) {
        if re.MatchString(sentence) {
            boredoms++
        }
    }
    return boredoms
}