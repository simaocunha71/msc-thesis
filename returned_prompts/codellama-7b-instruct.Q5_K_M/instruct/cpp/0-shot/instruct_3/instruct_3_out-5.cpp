
    #include <stdio.h>
    #include <string.h>

    int main(void) {
        int i;
        char key[] = "abcdefghij";
        char text[100];
        char cipher[100];

        printf("Enter a string: ");
        fgets(text, 100, stdin);

        for (i = 0; i < strlen(text); i++) {
            if (text[i] >= 'a' && text[i] <= 'z')
                cipher[i] = key[(text[i] - 'a') % 9 + 'a'];
            else if (text[i] >= 'A' && text[i] <= 'Z')
                cipher[i] = key[(text[i] - 'A') % 9 + 'A'];
            else
                cipher[i] = text[i];
        }

        printf("Encrypted string: %s\n", cipher);

        return 0;
    }

