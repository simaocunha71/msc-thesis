*/

#include <stdint.h>
#include <string.h>

#define MD4_BLOCK_SIZE 64
#define MD4_HASH_SIZE 16
#define MD4_STATE_WORDS 4

typedef struct {
    uint32_t state[MD4_STATE_WORDS];
    uint32_t count[2];
    uint8_t buffer[MD4_BLOCK_SIZE];
} md4_context;

void md4_init(md4_context *context) {
    context->state[0] = 0x67452301;
    context->state[1] = 0xEFCDAB89;
    context->state[2] = 0x98BADCFE;
    context->state[3] = 0x10325476;

    context->count[0] = 0;
    context->count[1] = 0;
}

void md4_update(md4_context *context, const uint8_t *input, size_t length) {
    uint32_t index = (uint32_t)((context->count[0] >> 3) & 0x3F);
    uint32_t part = 64 - index;

    context->count[0] += (uint32_t)length;
    context->count[1] += (context->count[0] < index);

    if (length >= part) {
        memcpy(&context->buffer[index], input, part);
        input += part;
        length -= part;

        // Process full 64-byte chunks
        while (length >= MD4_BLOCK_SIZE) {
            // Process the chunk
            // ...

            input += MD4_BLOCK_SIZE;
            length -= MD4_BLOCK_SIZE;
        }
    }

    // Save the remaining part
    memcpy(&context->buffer[index], input, length);
}

void md4_final(md4_context *context, uint8_t digest