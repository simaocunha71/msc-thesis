
#include <stdint.h>
#include <string.h>

#define MD4_BLOCK_SIZE 64
#define MD4_DIGEST_SIZE 16

void md4_transform(uint32_t *state, const uint8_t *block);

void md4_init(MD4_CTX *context)
{
    context->count = 0;
    context->state[0] = 0x67452301;
    context->state[1] = 0xEFCDAB89;
    context->state[2] = 0x98BADCFE;
    context->state[3] = 0x10325476;
}

void md4_update(MD4_CTX *context, const uint8_t *input, uint32_t len)
{
    uint32_t i, index, partLen;

    index = (uint32_t)((context->count & 0x3F) >> 3);

    context->count += len;
    partLen = 64 - index;

    if (len >= partLen) {
        memcpy(&context->buffer[index], input, partLen);
        md4_transform(context->state, context->buffer);

        for (i = partLen; i + 64 <= len; i += 64) {
            md4_transform(context->state, &input[i]);
        }

        index = 0;
    } else {
        index += len;
    }

    memcpy(&context->buffer[index], &input[i], len - i);
}

void md4_final(MD4_CTX *context, uint8_t digest[MD4_DIGEST_SIZE])
{
    uint32_t index, padLen;

    index = (uint32_t)((context->count & 0x3F) >> 3);
    padLen = (index < 56) ? (56 - index) : (120 - index);

    md4_