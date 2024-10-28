
	#define MD4_Init(c) FIPS_MD4_Init(c)
	#define MD4_Update(c,d,n) FIPS_MD4_Update(c,d,n)
	#define MD4_Final(d,c) FIPS_MD4_Final(d,c)
#else
	#define MD4_Init(c) MD4Init(c)
	#define MD4_Update(c,d,n) MD4Update(c,d,n)
	#define MD4_Final(d,c) MD4Final(d,c)
#endif

void MD4Init(MD4_CTX *c)
{
	c->A = 0x67452301;
	c->B = 0xefcdab89;
	c->C = 0x98badcfe;
	c->D = 0x10325476;
	c->Nl = 0;
	c->Nh = 0;
	c->num = 0;
}

void MD4Update(MD4_CTX *c, const MD4_LBLOCK *d, unsigned int n)
{
	MD4_LONG *p;
	unsigned int i,j;

	j = (c->Nl >> 3) % MD4_LBLOCK;
	c->Nl += n << 3;
	if ((c->Nl < n << 3) || (j < (n & ~MD4_LBLOCK))) ++c->Nh;

	p = c->data;
	for (i = 0; i < j; ++i)
		*p++ ^= d[i];
	for (; i < n; ++i)
		*p++ ^= d[i];
	for (i = 0; i < n; ++i)
		*p++ = d[i];
	c->num += n;
}

void MD4Final(MD4_CTX *c, MD4_LBLOCK *d)
{
	unsigned int i,j;
	MD4_LONG *p;

	j = (c->Nl >> 3) %