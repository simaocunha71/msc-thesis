    #include <stdio.h>
    #include <string.h>

    int main(int argc, char **argv) {
        char key[] = "ABCDEFGHI";
        char encrypted[256];

        if (argc != 2) {
            printf("Usage: %s <string>\n", argv[0]);
            return 1;
        }

        strcpy(encrypted, argv[1]);
        for (size_t i = 0; i < strlen(encrypted); i++) {
            char c = encrypted[i];
            if (c >= 'A' && c <= 'Z') {
                c = key[c - 'A'];
            } else if (c >= 'a' && c <= 'z') {
                c = key[c - 'a'];
            }
            encrypted[i] = c;
        }
        printf("%s\n", encrypted);
        return 0;
    }

