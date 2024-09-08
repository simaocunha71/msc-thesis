    if(s0.size()!=s1.size())
        return false;
    sort(s0.begin(),s0.end());
    sort(s1.begin(),s1.end());
    return s0==s1;
}
int main(int argc, char const *argv[]) {
    printf("%d\n",(same_chars("eabcdzzzz", "dddzzzzzzzddeddabc")));
    printf("%d\n",(same_chars("abcd", "dddddddabc")));
    printf("%d\n",(same_chars("dddddddabc", "abcd")));
    printf("%d\n",(same_chars("eabcd", "dddddddabc")));
    printf("%d\n",(same_chars("abcd", "dddddddabce")));
    printf("%d\n",(same_chars("eabcdzzzz", "dddzzzzzzzddddabc")));
    return 0;
}
