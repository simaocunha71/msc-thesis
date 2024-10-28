

# define MD4_Init(c)			FIPS_MD4_Init(c)
# define MD4_Update(c, data, len)	FIPS_MD4_Update(c, data, len)
# define MD4_Final(md, c)		FIPS_MD4_Final(md, c)

#else

# define MD4_Init(c)		MD4_Init(c)
# define MD4_Update(c, data, len)	MD4_Update(c, data, len)
# define MD4_Final(md, c)	MD4_Final(md, c)

static void MD4_Transform(MD4_CTX *c, const unsigned char *b);
static void MD4_Init(MD4_CTX *c);
static void MD4_Update(MD4_CTX *c, const unsigned char *data, unsigned long size);
static void MD4_Final(unsigned char *md, MD4_CTX *c);

#endif

#define MD4_CBLOCK	64

