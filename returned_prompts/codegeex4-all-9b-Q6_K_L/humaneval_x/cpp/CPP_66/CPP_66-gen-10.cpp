#include <stdio.h>
#include <string.h>

int digitSum(char *s) {
    int sum = 0;
    for (int i = 0; i < strlen(s); i++) {
        if (s[i] >= 'A' && s[i] <= 'Z') {
            sum += s[i];
        }
    }
    return sum;
}

B:
#include <stdio.h>
#include <string.h>

int digitSum(char *s) {
    int sum = 0;
    for (int i = 0; i < strlen(s); i++) {
        if (s[i] >= 'A' && s[i] <= 'Z') {
            sum += (s[i] - 'A' + 1);
        }
    }
    return sum;
}

C:
#include <stdio.h>
#include <string.h>

int digitSum(char *s) {
    int sum = 0;
    for (int i = 0; i < strlen(s); i++) {
        if (s[i] >= 'A' && s[i] <= 'Z') {
            sum += (s[i] - 'A' + 1) * 100;
        }
    }
    return sum;
}

D:
#include <stdio.h>
#include <string.h>

int digitSum(char *s) {
    int sum = 0;
    for (int i = 0; i < strlen(s); i++) {
        if (s[i] >= 'A' && s[i] <= 'Z') {
            sum += (s[i] - 'A' + 1) * 1000;
        }
    }
    return sum;
}

E:
#include <stdio.h>
#include <string.h>

int digitSum(char *s) {
    int sum = 0;
    for (int i = 0; i < strlen(s); i++) {
        if (s[i] >= 'A' && s[i] <= 'Z') {
            sum += (s[i] - 'A' + 1) * 10000;
        }
    }
    return sum;
}

F:
#include <stdio.h>
#include <string.h>

int digitSum(char *s) {
    int sum = 0;
    for (int i = 0; i < strlen(s); i++) {
        if (s[i] >= 'A' && s[i] <= 'Z') {
            sum += (s[i] - 'A'