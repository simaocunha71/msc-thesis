#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <openssl/md5.h>
#include <openssl/sha.h>

void hash_buffer(const void *buffer, size_t length, unsigned char *hash, int hash_type)
{
    switch (hash_type) {
        case 1: // MD5
            MD5(buffer, length, hash);
            break;
        case 2: // SHA
            SHA1(buffer, length, hash);
            break;
        default:
            fprintf(stderr, "Invalid hash type\n");
            exit(EXIT_FAILURE);
    }
}

int main()
{
    const char *message = "Hello, world!";
    unsigned char hash[MD5_DIGEST_LENGTH];
    hash_buffer(message, strlen(message), hash, 1);
    printf("MD5 hash: ");
    for (int i = 0; i < MD5_DIGEST_LENGTH; i++) {
        printf("%02x", hash[i]);
    }
    printf("\n");
    return 0;
}