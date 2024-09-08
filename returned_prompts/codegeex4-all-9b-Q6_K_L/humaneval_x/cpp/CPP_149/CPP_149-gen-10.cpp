#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

#define MAX_WORD_LENGTH 100

void sort_and_remove_odd_length_words(char ***words, int *num_words) {
    qsort(*words, *num_words, sizeof(char *), compare_strings);

    int i, j;
    for (i = 0, j = 0; i < *num_words; i++) {
        if (strlen((*words)[i]) % 2 == 0) {
            (*words)[j] = (*words)[i];
            j++;
        }
    }

    *num_words = j;
}

int compare_strings(const void *a, const void *b) {
    const char *str1 = *((const char **)a);
    const char *str2 = *((const char **)b);

    int len1 = strlen(str1);
    int len2 = strlen(str2);

    if (len1 < len2)
        return -1;
    else if (len1 > len2)
        return 1;
    else
        return strcmp(str1, str2);
}

void free_words(char ***words, int num_words) {
    int i;
    for (i = 0; i < num_words; i++) {
        free((*words)[i]);
    }

    free(*words);
}

char ***vector_sort(char **words, int num_words) {
    sort_and_remove_odd_length_words(&words, &num_words);

    char ***result = (char ***)malloc(num_words * sizeof(char **));
    int i;
    for (i = 0; i < num_words; i++) {
        result[i] = (char **)malloc(2 * sizeof(char *));
        result[i][0] = words[i];
        result[i][1] = NULL;
    }

    return result;
}

int main() {
    char *words[] = {"aa", "a", "aaa"};
    int num_words = 3;
    char ***sorted_words = vector_sort(words, num_words);

    assert(strcmp(sorted_words[0][0], "aa") == 0);

    char *words2[] = {"ab", "a", "aaa", "cd"};
    num_words = 4;
    sorted_words = vector_sort(words2, num_words);

    assert(strcmp(sorted_words[0][0], "ab") == 0);
    assert(strcmp(sorted_words[1][0], "cd") == 