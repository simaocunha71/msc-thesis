    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>
    #include <openssl/md5.h>
    #include <openssl/sha.h>
    void *hash_function(const void *input, size_t input_size, const char *algorithm) {
        void *hash;
        switch (strcmp(algorithm, "MD5")) {
            case 0:
                hash = (void *)MD5((unsigned char *)input, input_size, (unsigned char *)hash);
                break;
            case 1:
                hash = (void *)SHA1((unsigned char *)input, input_size, (unsigned char *)hash);
                break;
            case 2:
                hash = (void *)SHA256((unsigned char *)input, input_size, (unsigned char *)hash);
                break;
            case 3:
                hash = (void *)MD2((unsigned char *)input, input_size, (unsigned char *)hash);
                break;
            default:
                hash = NULL;
        }
        return hash;
    }   #include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <openssl/md5.h>
#include <openssl/sha.h>

void *hash_function(const void *input, size_t input_size, const char *algorithm) {
    void *hash;
    switch (strcmp(algorithm, "MD5")) {
        case 0:
            hash = (void *)MD5((unsigned char *)input, input_size, (unsigned char *)hash);
            break;
        case 1:
            hash = (void *)SHA1((unsigned char *)input, input_size, (unsigned char *)hash);
            break;
        case 2:
            hash = (void *)SHA256((unsigned char *)input, input_size, (unsigned char *)hash);
            break;
        case 3:
            hash = (void *)MD2((unsigned char *)input, input_size, (unsigned char *)hash);
            break;
        default:
            hash = NULL;
    }
    return hash;
} #include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <openssl/md5.h>
#include <openssl/sha.h>

void *hash_function(const void *input, size_t input_size, const char *algorithm) {
    void *hash;
    switch (strcmp(algorithm, "MD5")) {
        case 0:
            hash = (void *)MD5((unsigned char *)input, input_size