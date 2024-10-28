void MD4(message, message_len, hash) {
    unsigned int state[4] = {0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476};
    unsigned int i;
    unsigned char *p, *end;

    p = message;
    end = p + message_len;

    while (p < end) {
        unsigned int chunk[16];
        int j;

        for (j = 0; j < 16; j++) {
            chunk[j] = (p[j*4+3] << 24) | (p[j*4+2] << 16) |
                       (p[j*4+1] << 8) | p[j*4];
        }

        state[0] += chunk[0] + chunk[4] + chunk[8] + chunk[12];
        state[1] += chunk[1] + chunk[5] + chunk[9] + chunk[13];
        state[2] += chunk[2] + chunk[6] + chunk[10] + chunk[14];
        state[3] += chunk[3] + chunk[7] + chunk[11] + chunk[15];

        for (i = 0; i < 64; i++) {
            unsigned int a = state[0];
            unsigned int b = state[1];
            unsigned int c = state[2];
            unsigned int d = state[3];

            a = (a >> 3) | (a << 29);
            a += ((b & c) | (~b & d)) + 0x5a827999;
            b = (b >> 10) | (b << 22);
            b += (a & b) | (a & c) | (b & d) + 0x5a83298;
            c = (c >> 15) | (c << 17);
            c += (b & c) | (a & b) | (c & d) + 0x6b0644b;
            d = (d >> 21) | (d << 11);
            d += (c & d) | (a & c) | (b & d) + 0x6b0942f;

            state[0] = a;
            state[1] = b;
            state[2] =