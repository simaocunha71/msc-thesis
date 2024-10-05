    sort(s0.begin(),s0.end());
    sort(s1.begin(),s1.end());
B:
    return s0==s1;
}
int main(){
    printf(same_chars("eabcdzzzz", "dddzzzzzzzddeddabc") ? "true\n" : "false\n");
    printf(same_chars("abcd", "dddddddabc") ? "true\n" : "false\n");
    printf(same_chars("dddddddabc", "abcd") ? "true\n" : "false\n");
    printf(same_chars("eabcd", "dddddddabc") ? "true\n" : "false\n");
    printf(same_chars("abcd", "dddddddabce") ? "true\n" : "false\n");
    printf(same_chars("eabcdzzzz", "dddzzzzzzzddddabc") ? "true\n" : "false\n");