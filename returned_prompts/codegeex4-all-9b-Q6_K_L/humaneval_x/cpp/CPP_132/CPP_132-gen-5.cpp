#include <stdio.h>
#include <stdlib.h>
#include <string.h>

bool is_nested(char* str) {
    int open = 0;
    int close = 0;

    for (int i = 0; i < strlen(str); i++) {
        if (str[i] == '[') {
            open++;
        } else if (str[i] == ']') {
            close++;
        }

        if (close > open) {
            return false;
        }
    }

    return open == close;
}

int main() {
    char* test1 = "[[]]";
    char* test2 = "[]]]]]]][[[[[]";
    char* test3 = "[][]";
    char* test4 = "[]";
    char* test5 = "[[][]]";
    char* test6 = "[[]][[";

    printf("is_nested(\"%s\") ➞ %s\n", test1, is_nested(test1) ? "true" : "false");
    printf("is_nested(\"%s\") ➞ %s\n", test2, is_nested(test2) ? "true" : "false");
    printf("is_nested(\"%s\") ➞ %s\n", test3, is_nested(test3) ? "true" : "false");
    printf("is_nested(\"%s\") ➞ %s\n", test4, is_nested(test4) ? "true" : "false");
    printf("is_nested(\"%s\") ➞ %s\n", test5, is_nested(test5) ? "true" : "false");
    printf("is_nested(\"%s\") ➞ %s\n", test6, is_nested(test6) ? "true" : "false");

    return 0;
}

B:
#include <stdbool.h>
#include <stdio.h>
#include <string.h>

bool is_nested(const char* str) {
    int depth = 0;
    int max_depth = 0;

    for (int i = 0; str[i] != '\0'; i++) {
        if (str[i] == '[') {
            depth++;
            if (depth > max_depth) {
                max_depth = depth;
            }
        } else if (str[i] == ']') {
            depth--;
            if (depth < 0) {
                return false;
            }
        }
    }

    return max_depth > 1;
}

int main() {
    const char* test1 = "[[]]";
