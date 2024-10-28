
    This is a very basic implementation of the MD4 algorithm.

    This code is based on the description on Wikipedia:
    https://en.wikipedia.org/wiki/MD4#MD4_pseudocode

    And the code from the RFC:
    https://tools.ietf.org/html/rfc1320

    The code is not optimized for speed or memory usage.
*/

#include <stdint.h>

void md4(const uint8_t *message, size_t message_length, uint8_t *output)
{
    uint32_t a = 0x67452301;
    uint32_t b = 0xefcdab89;
    uint32_t c = 0x98badcfe;
    uint32_t d = 0x10325476;

    uint32_t bytes_processed = 0;
    uint32_t block_index = 0;

    uint8_t block[64];

    while (bytes_processed + 64 <= message_length) {
        for (uint32_t i = 0; i < 64; i++) {
            block[i] = message[block_index + i];
        }
        block_index += 64;

        uint32_t x[16];
        for (uint32_t i = 0; i < 16; i++) {
            x[i] = (block[i * 4 + 0] << 24) | (block[i * 4 + 1] << 16) | (block[i * 4 + 2] << 8) | block[i * 4 + 3];
        }

        uint32_t a_old = a;
        uint32_t b_old = b;
        uint32_t c_old = c;
        uint32_t d_old = d;

        a += (x[0] + (x[1] & (x[2] ^ x[3])));
