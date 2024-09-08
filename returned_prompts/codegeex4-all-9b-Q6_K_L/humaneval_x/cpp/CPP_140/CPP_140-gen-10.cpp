#include <stdio.h>
#include <string.h>

int main(void) {
    char str[] = "Example   3";
    char *p = str;
    char *q = str;

    while (*q) {
        if (*q == ' ') {
            if (*(q - 1) != ' ') {
                *p++ = '_';
            }
        } else {
            *p++ = *q;
        }
        q++;
    }

    if (p > str && *(p - 1) == ' ') {
        p--;
        *p = '\0';
    }

    printf("%s\n", str);
    return 0;
}

B:
#include <stdio.h>
#include <string.h>

int main(void) {
    char str[] = "Example   3";
    char *p = str;
    char *q = str;

    while (*q) {
        if (*q == ' ') {
            if (*(q - 1) != ' ') {
                *p++ = '_';
            }
            if (*(q + 1) != ' ') {
                *p++ = '-';
            }
        } else {
            *p++ = *q;
        }
        q++;
    }

    if (p > str && *(p - 1) == ' ') {
        p--;
        *p = '\0';
    }

    printf("%s\n", str);
    return 0;
}

C:
#include <stdio.h>
#include <string.h>

int main(void) {
    char str[] = "Example   3";
    char *p = str;
    char *q = str;

    while (*q) {
        if (*q == ' ') {
            if (*(q - 1) != ' ') {
                *p++ = '_';
            }
            if (*(q + 1) != ' ') {
                *p++ = '-';
            }
        } else {
            *p++ = *q;
        }
        q++;
    }

    if (p > str && *(p - 1) != ' ') {
        p--;
        *p = '\0';
    }

    printf("%s\n", str);
    return 0;
}

D:
#include <stdio.h>
#include <string.h>

int main(void) {
    char str[] = "Example   3";
    char *p = str;
    char *q = str;

    while (*q) {
        if (*q == ' ') {
           