#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int fruit_distribution(char s[100], int n) {
    char *token = strtok(s, " ");
    int apples = atoi(token);
    token = strtok(NULL, " ");
    int oranges = atoi(token);
    int mangoes = n - apples - oranges;
    return mangoes;
}

