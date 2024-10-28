#include <stdio.h>
#include <string.h>

int main() {
    char key[10];
    char text[100];
    int i;

    printf("Enter the encryption key: ");
    fgets(key, 10, stdin);
    key[strcspn(key, "\n")] = 0;

    printf("Enter the text to encrypt: ");
    fgets(text, 100, stdin);
    text[strcspn(text, "\n")] = 0;

    for (i = 0; i < strlen(text); i++) {
        if (isalpha(text[i])) {
            text[i] = key[(text[i] - 'a') % 9];
        }
    }

    printf("Encrypted text: %s\n", text);

    return 0;
}