    #include <string.h>

    #define MD4_BLOCK_SIZE 64
    #define MD4_DIGEST_LENGTH 16

    #define F(x, y, z) ((x & y) | (~x & z))
    #define G(x, y, z) ((x & z) | (y & ~z))
    #define H(x, y, z) (x ^ y ^ z)
    #define I(x, y, z) (y ^ (x | ~z))

    #define LEFT_ROTATE(x, n) ((x << n) | (x >> (32 - n)))

    typedef struct {
        uint32_t state[4];
        uint32_t count[2];
        uint8_t buffer[MD4_BLOCK_SIZE];
    } MD4_CTX;

    void MD4_Init(MD4_CTX *context);
    void MD4_Update(MD4_CTX *context, const void *data, size_t len);
    void MD4_Final(uint8_t digest[MD4_DIGEST_LENGTH], MD4_CTX *context);

    void MD4_Transform(uint32_t state[4], const uint8_t block[MD4_BLOCK_SIZE]);

    void MD4_Init(MD4_CTX *context) {
        context->state[0] = 0x67452301;
        context->state[1] = 0xefcdab89;
        context->state[2] = 0x98badcfe;
        context->state[3] = 0x10325476;

        context->count[0] = 0;
        context->count[1] = 0;
    }

    void MD4_Update(MD4_CTX *context, const void *data, size_t len) {
        size_t i;
        uint32_t partLength;

        for (i = 0; i < len; ++i) {
            context->buffer