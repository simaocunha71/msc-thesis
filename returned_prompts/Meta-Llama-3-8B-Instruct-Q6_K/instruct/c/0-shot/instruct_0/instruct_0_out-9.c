    ```c
    void md4_process_block(uint32_t *state, const uint8_t *input, int len) {
        uint32_t a, b, c, d;
        uint32_t x;
        int i;

        a = state[0];
        b = state[1];
        c = state[2];
        d = state[3];

        for (i = 0; i < len; i++) {
            x = (a << 11) ^ (a >> 21) ^ ((a & 0x80000000) >> 1) + b + 0xd76aa478;
            a = b;
            b = c;
            c = d;
            d = (d + x + input[i]) & 0xffffffff;
        }

        state[0] = (state[0] + a) & 0xffffffff;
        state[1] = (state[1] + b) & 0xffffffff;
        state[2] = (state[2] + c) & 0xffffffff;
        state[3] = (state[3] + d) & 0xffffffff;
    }

    void md4_finalize(uint32_t *state) {
        state[0] = (state[0] + 0x67452301) & 0xffffffff;
        state[1] = (state[1] + 0xefcdab89) & 0xffffffff;
        state[2] = (state[2] + 0x98badcfe) & 0xffffffff;
        state[3] = (state[3] + 0x10325476) & 0xffffffff;
    }

    void md4_hash(uint32_t *state, const uint8_t *input, int len) {
        int i;
        uint8_t buffer[64];

        for (i = 0; i < len; i += 64) {
            memcpy(buffer, input + i, 64);
            md4_process_block(state, buffer, 64);
        }

        if (len % 64) {
            uint8_t last[64];
            memcpy(last, input + len - (len % 64), len % 64);
            memset(last + len % 64, 0, 64 - len % 64);
            md4_process_block(state, last, 64);
        }

        md4_finalize(state);
    }
    ```