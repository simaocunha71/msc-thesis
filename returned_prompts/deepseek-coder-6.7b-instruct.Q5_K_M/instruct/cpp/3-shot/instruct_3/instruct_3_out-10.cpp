#include <stdio.h>
#include <string.h>

#define KEY_LEN 9

void encrypt(char *text, char *key) {
    for (int i = 0; i < strlen(text); i++) {
        if (text[i] >= 'a' && text[i] <= 'z') {
            text[i] = key[(text[i] - 'a') % KEY_LEN];
        } else if (text[i] >= 'A' && text[i] <= 'Z') {
            text[i] = key[(text[i] - 'A') % KEY_LEN] - 'a' + 'A';
        }
    }
}

int main() {
    char text[100], key[KEY_LEN + 1];
    printf("Enter text: ");
    fgets(text, sizeof(text), stdin);
    printf("Enter key: ");
    fgets(key, sizeof(key), stdin);
    encrypt(text, key);
    printf("Encrypted text: %s", text);
    return 0;
}

