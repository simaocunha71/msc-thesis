#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <assert.h>

char* fix_spaces(char* text) {
    int len = strlen(text);
    int space_count = 0;
    char* result = malloc(len * 2 + 1);
    int j = 0;

    for (int i = 0; i < len; i++) {
        if (text[i] == ' ') {
            space_count++;
            if (space_count == 3) {
                result[j++] = '-';
                space_count = 0;
            }
        } else {
            if (space_count > 0) {
                space_count = 0;
                result[j++] = '_';
            }
            result[j++] = text[i];
        }
    }

    if (space_count > 0) {
        result[j++] = '_';
    }

    result[j] = '\0';
    return result;
}

int main() {
    char* test1 = "Example";
    assert(strcmp(fix_spaces(test1), "Example") == 0);

    char* test2 = "Example 1";
    assert(strcmp(fix_spaces(test2), "Example_1") == 0);

    char* test3 = " Example 2";
    assert(strcmp(fix_spaces(test3), "_Example_2") == 0);

    char* test4 = " Example   3";
    assert(strcmp(fix_spaces(test4), "_Example-3") == 0);

    printf("All tests passed!\n");
    return 0;
}

B:
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <assert.h>

char* fix_spaces(char* text) {
    char* result = malloc(strlen(text) * 2 + 1);
    int j = 0;

    for (int i = 0; i < strlen(text); i++) {
        if (text[i] == ' ') {
            if (j > 0 && result[j - 1] == '_') {
                continue;
            } else {
                result[j++] = '_';
            }
        } else {
            result[j++] = text[i];
        }
    }

    result[j] = '\0';
    return result;
}

int main() {
    char* test1 = "Example";
    assert(strcmp(fix_spaces(test1), "Example") == 0);

    char*