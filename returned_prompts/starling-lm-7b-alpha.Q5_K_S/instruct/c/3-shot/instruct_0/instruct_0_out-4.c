{
    const uint32_t K[] = {
        0xd9d9d9d9u, 0x70e0e0e0u, 0xbadc0de, 0x01234567u
    };
    uint32_t h[4];
    uint32_t x[16];
    uint32_t a, b, c, d;
    uint32_t t1, t2;
    const uint32_t *w;
    unsigned int i, j;

    for (i = 0; i < 4; i++) {
        h[i] = 0u;
    }
    while (len % 64 != 0u) {
        h[0] += data[len - 1u];
        len--;
    }
    for (i = 0; i < 16; i++) {
        x[i] = 0u;
    }
    for (i = 0; i < len; i += 64u) {
        for (j = 0; j < 16; j++) {
            x[j] = h[j];
        }
        for (j = 0; j < 16; j++) {
            w = K + j;
            t1 = x[j] + (*w ^ x[j - 4u] ^ rotl32(x[j - 12u], 32u) ^ rotl32(x[j - 8u], 16u));
            t2 = *w + x[j - 7u] + x[j - 15u] + x[j - 2u] + x[j - 16u];
            x[j] = t1 + rotl32(t2, 32u);
        }
        for (j = 0; j < 4; j++) {
            h[j] += x[j];
        }
    }
    for (i = 0; i < 4; i++) {
        data[i] = h[i];
    }
}

