#include <stdint.h>
#include <string.h>

typedef struct {
    uint32_t a, b, c, d;
    uint64_t length;
} md4_context;

void md4_init(md4_context *ctx) {
    ctx->a = 0x67452301;
    ctx->b = 0xEFCDAB89;
    ctx->c = 0x98BADCFE;
    ctx->d = 0x10325476;
    ctx->length = 0;
}

void md4_update(md4_context *ctx, const uint8_t *data, size_t len) {
    while (len > 0) {
        size_t chunk_len = (len < 64) ? len : 64;
        uint8_t chunk[64];
        memcpy(chunk, data, chunk_len);
        data += chunk_len;
        len -= chunk_len;
        ctx->length += chunk_len * 8;

        uint32_t aa = ctx->a, bb = ctx->b, cc = ctx->c, dd = ctx->d;

        for (size_t i = 0; i < chunk_len; i += 4) {
            uint32_t x = chunk[i] | (chunk[i+1] << 8) | (chunk[i+2] << 16) | (chunk[i+3] << 24);

            uint32_t f, g;
            if (i < 16) {
                f = (bb & cc) | ((~bb) & dd);
                g = i;
            } else if (i < 32) {
                f = (bb & dd) | (cc & (~dd));
                g = (5*i + 1) % 16;
            } else if (i < 48) {
                f = bb ^ cc ^ dd;
                g = (3*i + 5) % 16;
            } else {
                f = cc ^ (bb | (~dd));
                g = (7*i) % 16;
            }

            uint32_t tmp = dd;
            dd = cc;
            cc = bb;
            bb = bb + leftrotate((aa + f + k[i] + x), s[i]);
            aa = tmp;
        }

        ctx->a += aa;
        ctx->b += bb;
        ctx->c += cc;
        ctx->d += dd;
    }
}

void md4_final(md4_context