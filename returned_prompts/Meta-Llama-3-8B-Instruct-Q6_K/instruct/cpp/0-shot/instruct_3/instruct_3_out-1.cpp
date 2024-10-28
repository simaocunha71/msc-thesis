    #include <stdio.h>
    #include <string.h>
    #include <ctype.h>

    char *encrypt(char *str, char *key) {
        int i = 0;
        char *pstr = str;
        char *pkey = key;
        char *ret = (char *)malloc(strlen(str) + 1);

        while (*pstr) {
            if (isalpha(*pstr)) {
                char c = tolower(*pstr);
                if (c >= 'a' && c <= 'z') {
                    c = (c - 'a' + *pkey - 'a') % 26 + 'a';
                } else if (c >= 'A' && c <= 'Z') {
                    c = (c - 'A' + *pkey - 'a') % 26 + 'A';
                }
                *ret++ = c;
            } else {
                *ret++ = *pstr;
            }
            pstr++;
            pkey++;
            if (pkey == key + 9) pkey = key;
        }
        *ret = '\0';
        return ret;
    }

    int main() {
        char str[81];
        char key[10];
        printf("Enter the text to encrypt: ");
        fgets(str, 80, stdin);
        printf("Enter the encryption key: ");
        fgets(key, 9, stdin);
        str[strlen(str) - 1] = '\0';
        key[strlen(key) - 1] = '\0';
        char *encrypted = encrypt(str, key);
        printf("Encrypted text: %s\n", encrypted);
        free(encrypted);
        return 0;
    }  // 9 characters of the key, and then print the encrypted text. The encryption method should replace each letter in the original text with the corresponding letter in the key, wrapping around to the beginning of the key if necessary. The program should also handle the case where the original text contains letters that are not in the key.  // 9 characters of the key, and then print the encrypted text. The encryption method should replace each letter in the original text with the corresponding letter in the key, wrapping around to the beginning of the key if necessary. The program should also handle the case where the original text contains letters that are not in the key.  // 9 characters of the key, and then print the encrypted text. The encryption method should replace each