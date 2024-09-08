#include <stdio.h>
#include <stdbool.h>
#include <string.h>

bool is_nested(const char* str) {
    int open = 0;
    int close = 0;
    int i = 0;
    while (str[i] != '\0') {
        if (str[i] == '[') {
            open++;
        } else if (str[i] == ']') {
            close++;
        }
        if (close > open) {
            return true;
        }
        i++;
    }
    if (close == open) {
        return false;
    } else {
        return true;
    }
}

int main() {
    printf("%d\n", is_nested("[[]]")); // true
    printf("%d\n", is_nested("[]]]]]]][[[[[]")); // false
    printf("%d\n", is_nested("[][]")); // false
    printf("%d\n", is_nested("[]")); // false
    printf("%d\n", is_nested("[[][]]")); // true
    printf("%d\n", is_nested("[[]][[")); // true
    return 0;
}

B:
#include <stdbool.h>
#include <string.h>

bool is_nested(const char* str) {
    int open = 0;
    int close = 0;
    int i = 0;
    while (str[i] != '\0') {
        if (str[i] == '[') {
            open++;
        } else if (str[i] == ']') {
            close++;
        }
        if (close > open) {
            return true;
        }
        i++;
    }
    if (close == open) {
        return false;
    } else {
        return true;
    }
}

int main() {
    printf("%d\n", is_nested("[[]]")); // true
    printf("%d\n", is_nested("[]]]]]]][[[[[]")); // false
    printf("%d\n", is_nested("[][]")); // false
    printf("%d\n", is_nested("[]")); // false
    printf("%d\n", is_nested("[[][]]")); // true
    printf("%d\n", is_nested("[[]][[")); // true
    return 0;
}

C:
#include <stdio.h>
#include <stdbool.h>
#include <string.h>

bool is_nested(const char* str) {
    int open = 0;
    int close = 0;
    int i = 0;
    while (str