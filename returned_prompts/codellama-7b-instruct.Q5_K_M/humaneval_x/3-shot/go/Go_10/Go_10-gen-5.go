    if IsPalindrome(str) {
        return str
    }

    postfix := strings.Split(str, "")
    for i := 0; i < len(postfix); i++ {
        if IsPalindrome(postfix[i]) {
            rev_prefix := strings.Split(str[:len(str)-i], "")
            for j := 0; j < len(rev_prefix); j++ {
                if IsPalindrome(strings.Join(append(rev_prefix[j:], rev_prefix[j:]...), "")) {
                    return strings.Join(append(rev_prefix[j:], postfix[i:]...), "")
                }
            }
            break
        }
    }
    return ""
}



