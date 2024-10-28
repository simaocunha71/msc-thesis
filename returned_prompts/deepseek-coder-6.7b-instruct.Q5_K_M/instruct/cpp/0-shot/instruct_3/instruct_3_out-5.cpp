
    Here is an example of how the program should work:
    Input string: "HELLO WORLD"
    Key: "KEYKEYKEYKEY"
    Output: "EELLO WIRLD"

    Input string: "hello world"
    Key: "keykeykeykey"
    Output: "eeLLO wIRLD"

    Input string: "hello world"
    Key: "KEY"
    Output: "EELLO WORLD"
*/

#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define MAX_LEN 100

char* encrypt(char* text, char* key) {
    int len = strlen(text);
    for (int i = 0; i < len; i++) {
        if (isupper(text[i])) {
            text[i] = toupper(key[(text[i] - 'A') % strlen(key)]);
        } else if (islower(text[i])) {
            text[i] = tolower(key[(text[i] - 'a') % strlen(key)]);
        }
    }
    return text;
}

int main() {
    char text[MAX_LEN], key[MAX_LEN];
    printf("Enter the text: ");
    fgets(text, MAX_LEN, stdin);
    printf("Enter the key: ");
    fgets(key, MAX_LEN, stdin);
    printf("Encrypted text: %s", encrypt(text, key));
    return 0;
}

/*
    The program reads in a string of text and a key, encrypts the text using the key, and then prints the encrypted text. The encryption method replaces each letter in the original text with the corresponding letter in the key, wrapping around to the beginning of the key if necessary. The program also handles the case where the original text contains letters that are not in the key.
*/

/*
    The program reads in a string of text and a key, encrypts the text using the key, and then prints the encrypted text. The encryption method replaces each letter in the original