    #include <stdio.h>
    #include <string.h>
    #include <ctype.h>

    #define KEY_LENGTH 9
    #define MAX_TEXT_LENGTH 100

    char key[KEY_LENGTH] = "abcdefghi";

    int main() {
        char text[MAX_TEXT_LENGTH];
        char encryptedText[MAX_TEXT_LENGTH];

        printf("Enter a string of text: ");
        fgets(text, MAX_TEXT_LENGTH, stdin);

        int i;
        for (i = 0; i < strlen(text); i++) {
            if (isalpha(text[i])) {
                char c = tolower(text[i]);
                int index = c - 'a';
                encryptedText[i] = tolower(key[index % KEY_LENGTH]);
            } else {
                encryptedText[i] = text[i];
            }
        }

        encryptedText[i] = '\0';

        printf("Encrypted text: %s\n", encryptedText);

        return 0;
    }

