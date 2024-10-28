        #include <stdio.h>
        #include <stdlib.h>
        #include <string.h>
        #include <openssl/md5.h>
        #include <openssl/sha.h>

        unsigned char* hash(char* input, int length, char* algorithm) {
            unsigned char* output = NULL;
            int output_length;

            if (strcmp(algorithm, "MD5") == 0) {
                MD5_CTX ctx;
                MD5_Init(&ctx);
                MD5_Update(&ctx, input, length);
                MD5_Final(ctx.md5, &ctx);
                output = ctx.md5;
                output_length = 16;
            } else if (strcmp(algorithm, "SHA1") == 0) {
                SHA_CTX ctx;
                SHA1_Init(&ctx);
                SHA1_Update(&ctx, input, length);
                SHA1_Final(ctx.sha1, &ctx);
                output = ctx.sha1;
                output_length = 20;
            } else {
                printf("Unsupported algorithm\n");
                return NULL;
            }

            return output;
        }