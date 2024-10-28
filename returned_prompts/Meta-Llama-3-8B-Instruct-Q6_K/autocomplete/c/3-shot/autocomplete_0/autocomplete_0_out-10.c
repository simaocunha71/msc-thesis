#define MD4_DIGEST_LENGTH 16
#else
#define MD4_DIGEST_LENGTH 16
#endif

void MD4_Init(MD4_CTX *c)
    {
    c->A = 0x67452301;
    c->B = 0xefcdab89;
    c->C = 0x98badcfe;
    c->D = 0x10325476;
    c->num = 0;
    } 

