
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <openssl/md5.h>
#include <openssl/sha.h>

void hash_function(const unsigned char *input, size_t length, unsigned char *output, int algorithm) {
    switch (algorithm) {
        case 1: // MD2
            MD2(input, length, output);
            break;
        case 2: // MD4
            MD4(input, length, output);
            break;
        case 3: // MD5
            MD5(input, length, output);
            break;
        case 4: // SHA
            SHA1(input, length, output);
            break;
        default:
            printf("Invalid algorithm\n");
            exit(1);
    }
}

int main() {
    const unsigned char *input = "Hello, world!";
    size_t length = strlen((char *)input);
    unsigned char *output = (unsigned char *)malloc(MD5_DIGEST_LENGTH);

    hash_function(input, length, output, 3);

    printf("Hash value: ");
    for (int i = 0; i < MD5_DIGEST_LENGTH; i++) {
        printf("%02x", output[i]);
    }
    printf("\n");

    free(output);
    return 0;
}
```
