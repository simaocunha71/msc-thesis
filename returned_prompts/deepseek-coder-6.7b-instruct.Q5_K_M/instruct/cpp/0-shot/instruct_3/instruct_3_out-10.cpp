```c
#include <stdio.h>
#include <string.h>

#define KEY_LEN 9

void encrypt(char *text, char *key) {
    int text_len = strlen(text);
    for (int i = 0; i < text_len; i++) {
        if (text[i] >= 'a' && text[i] <= 'z') {
            text[i] = key[(text[i] - 'a') % KEY_LEN];
        } else if (text[i] >= 'A' && text[i] <= 'Z') {
            text[i] = key[(text[i] - 'A') % KEY_LEN] - 'a' + 'A';
        }
    }
}

int main() {
    char key[KEY_LEN + 1] = "ABCDEFGHI";
    char text[100];

    printf("Enter text: ");
    fgets(text, sizeof(text), stdin);

    encrypt(text, key);

    printf("Encrypted text: %s", text);

    return 0;
}
```
