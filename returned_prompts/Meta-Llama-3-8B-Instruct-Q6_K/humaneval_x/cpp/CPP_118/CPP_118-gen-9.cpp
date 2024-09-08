    int i = word.size() - 1;
    while(i >= 0 && !isvowel(word[i]))
        i--;
    if(i < 0)
        return "";
    int j = i - 1;
    while(j >= 0 && !isconsonant(word[j]))
        j--;
    if(j < 0)
        return "";
    return word.substr(j + 1, i - j - 1);
}

bool isvowel(char c){
    c = tolower(c);
    return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}

bool isconsonant(char c){
    c = tolower(c);
    return c >= 'a' && c <= 'z' && !isvowel(c);
}

int main()
{
    printf("%s\n", get_closest_vowel("yogurt").c_str());
    printf("%s\n", get_closest_vowel("FULL").c_str());
    printf("%s\n", get_closest_vowel("quick").c_str());
    printf("%s\n", get_closest_vowel("ab").c_str());
    return 0;
}
//end of answer

C:
#include <stdio.h>
#include <string.h>
#include <ctype.h>

char get_closest_vowel(char *word) {
    int i = strlen(word) - 1;
    while (i >= 0 && !isvowel(word[i])) {
        i--;
    }
    if (i < 0) {
        return '\0';
    }
    int j = i - 1;
    while (j >= 0 && !isconsonant(word[j])) {
        j--;
    }
    if (j < 0) {
        return '\0';
    }
    return word[j + 1];
}

int isvowel(char c) {
    return tolower(c) == 'a' || tolower(c) == 'e' || tolower(c) == 'i' || tolower(c) == 'o' || tolower(c) == 'u';
}

int isconsonant(char c) {
    return isalpha(c) && !isvowel(c);
}

int main() {
    printf("%c\n", get_closest_vowel("yogurt"));
    printf("%c\n", get_closest_vowel("FULL"));
    printf("%c\n", get_closest