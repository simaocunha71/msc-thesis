    sort(s0.begin(), s0.end());
    sort(s1.begin(), s1.end());
    return s0 == s1;
}

int main() {
    printf("%s\n", same_chars("eabcdzzzz", "dddzzzzzzzddeddabc") ? "true" : "false");
    printf("%s\n", same_chars("abcd", "dddddddabc") ? "true" : "false");
    printf("%s\n", same_chars("dddddddabc", "abcd") ? "true" : "false");
    printf("%s\n", same_chars("eabcd", "dddddddabc") ? "true" : "false");
    printf("%s\n", same_chars("abcd", "dddddddabce") ? "true" : "false");
    printf("%s\n", same_chars("eabcdzzzz", "dddzzzzzzzddddabc") ? "true" : "false");
    return 0;
}

*/
/*
