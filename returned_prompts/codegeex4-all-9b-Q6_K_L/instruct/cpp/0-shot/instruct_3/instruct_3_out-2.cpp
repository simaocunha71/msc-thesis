
```c
#include <stdio.h>
#include <string.h>

void encrypt(char *text, char *key) {
    int i, j;
    for (i = 0, j = 0; text[i] != '\0'; i++, j++) {
        if (j == strlen(key)) j = 0;
        if (text[i] >= 'a' && text[i] <= 'z') {
            text[i] = 'a' + (text[i] - 'a' + key[j] - 'a') % 26;
        } else if (text[i] >= 'A' && text[i] <= 'Z') {
            text[i] = 'A' + (text[i] - 'A' + key[j] - 'A') % 26;
        }
    }
}

int main() {
    char text[100], key[10];

    printf("Enter the text: ");
    fgets(text, sizeof(text), stdin);
    text[strcspn(text, "\n")] = 0;

    printf("Enter the key: ");
    fgets(key, sizeof(key), stdin);
    key[strcspn(key, "\n")] = 0;

    encrypt(text, key);

    printf("Encrypted text: %s\n", text);

    return 0;
}
```
