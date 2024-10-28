
The MD4 algorithm is defined in RFC 1320, and the following pseudo-code outlines the algorithm:

    Initialize the state with the initial values:
        a = 0x12345678, b = 0x87654321, c = 0xabcd1234, d = 0x4321f6a8

    For each 64-bit message word (or group of words) in the message, compute a series of intermediate hash values by applying a step function to the state and message words, and then add the intermediate hash value to the main hash value.

    Compute the final intermediate hash value for the last message word, and add it to the main hash value.

    Return the main hash value as the output.

Here's a rough outline of the algorithm in C:

    #include <stdint.h>
    #include <stdio.h>
    #include <string.h>

    typedef union {
        uint32_t v;
        uint8_t c[4];
    } u32;

    static void md4_step(uint32_t *state, const u32 *msg) {
        uint32_t a = state[0];
        uint32_t b = state[1];
        uint32_t c = state[2];
        uint32_t d = state[3];

        uint32_t tmp;

        tmp = d + a;
        tmp = tmp << 9;
        tmp = tmp + b;
        tmp = tmp << 3;
        tmp = tmp + c;
        tmp = tmp << 6;
        tmp = tmp + a;
        tmp = tmp << 11;
        tmp = tmp + d;
        tmp = tmp << 16;
        tmp = tmp + b;
        tmp = tmp << 23;
        tmp = tmp + c;
        tmp = tmp << 4;
        tmp = tmp + a;
        tmp = tmp << 13;
        tmp = tmp + d;
        tmp = tmp << 2;
        tmp = tmp +