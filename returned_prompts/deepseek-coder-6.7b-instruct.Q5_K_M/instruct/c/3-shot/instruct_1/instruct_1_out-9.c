#include <openssl/md2.h>
#include <openssl/md4.h>
#include <openssl/md5.h>
#include <openssl/sha.h>

unsigned char *hash_function(const char *algorithm, const void *buffer, size_t length, size_t *out_length)
{
    unsigned char *out = NULL;
    if (!strcmp(algorithm, "MD2")) {
        out = (unsigned char*)malloc(MD2_DIGEST_LENGTH);
        MD2((unsigned char*)buffer, length, out);
        *out_length = MD2_DIGEST_LENGTH;
    } else if (!strcmp(algorithm, "MD4")) {
        out = (unsigned char*)malloc(MD4_DIGEST_LENGTH);
        MD4((unsigned char*)buffer, length, out);
        *out_length = MD4_DIGEST_LENGTH;
    } else if (!strcmp(algorithm, "MD5")) {
        out = (unsigned char*)malloc(MD5_DIGEST_LENGTH);
        MD5((unsigned char*)buffer, length, out);
        *out_length = MD5_DIGEST_LENGTH;
    } else if (!strcmp(algorithm, "SHA")) {
        out = (unsigned char*)malloc(SHA_DIGEST_LENGTH);
        SHA((unsigned char*)buffer, length, out);
        *out_length = SHA_DIGEST_LENGTH;
    }
    return out;
}

