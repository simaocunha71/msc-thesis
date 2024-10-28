    #include <openssl/sha.h>
    #include <openssl/md2.h>
    #include <openssl/md4.h>
    #include <openssl/md5.h>

    unsigned char *hash_function(unsigned char *input, size_t length, char *algorithm) {
        unsigned char *hash_value = malloc(MD5_DIGEST_LENGTH);

        if (strcmp(algorithm, "MD2") == 0) {
            MD2_CTX context;
            MD2_Init(&context);
            MD2_Update(&context, input, length);
            MD2_Final(hash_value, &context);
        } else if (strcmp(algorithm, "MD4") == 0) {
            MD4_CTX context;
            MD4_Init(&context);
            MD4_Update(&context, input, length);
            MD4_Final(hash_value, &context);
        } else if (strcmp(algorithm, "MD5") == 0) {
            MD5_CTX context;
            MD5_Init(&context);
            MD5_Update(&context, input, length);
            MD5_Final(hash_value, &context);
        } else if (strcmp(algorithm, "SHA") == 0) {
            SHA_CTX context;
            SHA1_Init(&context);
            SHA1_Update(&context, input, length);
            SHA1_Final(hash_value, &context);
        } else {
            printf("Invalid algorithm\n");
            free(hash_value);
            return NULL;
        }

        return hash_value;
    }

