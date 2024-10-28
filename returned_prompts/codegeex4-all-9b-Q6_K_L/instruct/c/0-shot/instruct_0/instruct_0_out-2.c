
```c
#include <stdint.h>
#include <string.h>

void md4(uint8_t *message, size_t length, uint8_t *hash) {
    uint32_t A = 0x67452301;
    uint32_t B = 0xEFCDAB89;
    uint32_t C = 0x98BADCFE;
    uint32_t D = 0x10325476;

    uint8_t chunk[64];
    uint32_t K[64];
    uint32_t W[16];

    int i, j;

    for (i = 0; i < length; i += 64) {
        memcpy(chunk, &message[i], 64);

        for (j = 0; j < 16; j++) {
            W[j] = (chunk[4*j] << 24) | (chunk[4*j+1] << 16) | (chunk[4*j+2] << 8) | chunk[4*j+3];
        }

        for (j = 0; j < 64; j++) {
            K[j] = (uint32_t)j;
        }

        for (j = 0; j < 16; j++) {
            A += (B & C) | (~B & D);
            A = (A + W[j] + K[j]) & 0xFFFFFFFF;
            A = (A << 3) | (A >> 29);
            A += B;
            B = (B << 3) | (B >> 29);

            D += (A & B) | (~A & C);
            D = (D + W[(j+5) % 16] + K[(j+5) % 16]) & 0xFFFFFFFF;
            D = (D << 9) | (D >> 23);
            D += A;
            A = (A << 9) | (A >> 23);

            C += (D & A) | (~D & B);
            C = (C + W[(j+10) % 16] + K[(j+10) % 16]) & 0xFFFFFFFF;
            C = (C << 11) | (C >> 21);
            C += D;
            D = (D << 11) | (D >> 21);

            B += (C & D) | (~C & A);
