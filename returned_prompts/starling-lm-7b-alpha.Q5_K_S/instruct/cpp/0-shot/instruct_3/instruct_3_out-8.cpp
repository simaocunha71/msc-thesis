    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>

    int main(int argc, char *argv[]) {
        char *key, *text, *encrypted;
        int i, j, k;

        if (argc < 3) {
            printf("Usage: %s key text\n", argv[0]);
            return 1;
        }

        key = argv[1];
        text = argv[2];
        encrypted = malloc(strlen(text) + 1);
        if (encrypted == NULL) {
            printf("Memory allocation failed\n");
            return 1;
        }

        for (i = 0; i < strlen(text); i++) {
            if (isalpha(text[i])) {
                j = (key[i % strlen(key)] + 0x20) - (0x61 + islower(text[i]));
                if (j < 0) j += 0x26;
                encrypted[i] = (char)j;
            } else {
                encrypted[i] = text[i];
            }
        }
        encrypted[strlen(text)] = '\0';
        printf("%s\n", encrypted);
        free(encrypted);
        return 0;
    }

