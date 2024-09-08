    string s = b;
    for(int i = 0; i < b.length(); i++){
        s = s.substr(1) + s[0];
        if(a.find(s) != string::npos){
            return true;
        }
    }
    return false;
}

int main() {
    string a = "abcd";
    string b = "abd";
    if(cycpattern_check(a,b))
        printf("true\n");
    else
        printf("false\n");

    a = "hello";
    b = "ell";
    if(cycpattern_check(a,b))
        printf("true\n");
    else
        printf("false\n");

    a = "whassup";
    b = "psus";
    if(cycpattern_check(a,b))
        printf("true\n");
    else
        printf("false\n");

    a = "abab";
    b = "baa";
    if(cycpattern_check(a,b))
        printf("true\n");
    else
        printf("false\n");

    a = "efef";
    b = "eeff";
    if(cycpattern_check(a,b))
        printf("true\n");
    else
        printf("false\n");

    a = "himenss";
    b = "simen";
    if(cycpattern_check(a,b))
        printf("true\n");
    else
        printf("false\n");

    return 0;
}

B:
    #include <stdio.h>
#include <string.h>

int cycpattern_check(const char *a, const char *b) {
    int len_a = strlen(a);
    int len_b = strlen(b);

    for (int i = 0; i < len_b; i++) {
        char *s = (char *)malloc((len_b + 1) * sizeof(char));
        for (int j = 0; j < len_b; j++) {
            s[j] = b[(i + j) % len_b];
        }
        s[len_b] = '\0';
        if (strstr(a, s) != NULL) {
            free(s);
            return 1;
        }
        free(s);
    }
    return 0;
}

int main() {
    printf("%d\n", cycpattern_check("abcd", "abd")); // 0
    printf("%d\n", cycpattern_check("hello", "ell")); // 1
    printf("%d\n", cycpattern_check("whassup",