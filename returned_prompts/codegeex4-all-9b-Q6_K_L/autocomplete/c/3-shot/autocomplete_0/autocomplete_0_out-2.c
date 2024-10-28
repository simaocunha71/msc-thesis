#endif
#define MD4_CBLOCK    64
#define MD4_LBLOCK    (MD4_CBLOCK/4)
#define MD4_DIGEST_LENGTH 16

#if defined(OPENSSL_NO_MD4) || defined(OPENSSL_FIPS)
void MD4_Init(MD4_CTX *c);
void MD4_Update(MD4_CTX *c, const unsigned char *in, unsigned long inl);
void MD4_Final(unsigned char *out, MD4_CTX *c);
#else
void MD4_Init(MD4_CTX *c);
void MD4_Transform(MD4_CTX *c, const unsigned char [MD4_CBLOCK]);
void MD4_Update(MD4_CTX *c, const unsigned char *in, unsigned long inl);
void MD4_Final(unsigned char *out, MD4_CTX *c);
#endif

