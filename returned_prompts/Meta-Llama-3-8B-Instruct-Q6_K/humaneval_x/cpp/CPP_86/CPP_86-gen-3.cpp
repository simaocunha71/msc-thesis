

C:
```c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

char* anti_shuffle(char* str) {
    char* res = (char*)malloc(strlen(str) + 1);
    char* temp = (char*)malloc(strlen(str) + 1);
    strcpy(res, str);
    int i = 0;
    while (res[i] != '\0') {
        if (res[i] == ' ') {
            i++;
            continue;
        }
        temp[0] = '\0';
        while (res[i] != ' ' && res[i] != '\0') {
            temp = (char*)realloc(temp, strlen(temp) + 2);
            temp = strcat(temp, (char*)&res[i]);
            res[i] = tolower(res[i]);
            i++;
        }
        char* t = (char*)malloc(strlen(temp) + 1);
        for (int j = 0; j < strlen(temp); j++) {
            t[j] = temp[j];
        }
        t = strcat(t, (char*)"\0");
        char* s = t;
        while (*s) {
            char* p = s;
            while (*p && isalpha(*p)) {
                p++;
            }
            *p = '\0';
            s = p;
        }
        char* q = s;
        while (*q) {
            q++;
        }
        q--;
        while (q > s) {
            char c = *q;
            *q = *s;
            *s = c;
            s++;
            q--;
        }
        res = (char*)realloc