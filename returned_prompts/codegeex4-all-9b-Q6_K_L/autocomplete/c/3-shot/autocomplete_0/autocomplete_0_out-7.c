
void MD4_Update_FIPS(MD4_CTX *c, const unsigned char *data, size_t len);
#endif

void MD4_Update(MD4_CTX *c, const unsigned char *data, size_t len)
	{
	unsigned int i;
	size_t n;
	n = len & 0x3F;
	if (n != 0) {
		for (i = 0; i < n; i++)
			c->data[c->num / 4] |= (unsigned long)(data[i])
				<< ((c->num % 4) * 8);
		c->num += n;
		if (c->num >= MD4_BLOCK) {
			MD4_Transform(c->A,c->B,c->C,c->D,c->data);
			c->num -= MD4_BLOCK;
		}
		data += n;
		len -= n;
	}
	for ( ; len >= MD4_BLOCK; len -= MD4_BLOCK, data += MD4_BLOCK) {
		MD4_Transform(c->A,c->B,c->C,c->D,(unsigned long *)data);
	}
	n = len & 0x3F;
	if (n != 0) {
		c->data[0] = 0;
		c->data[1] = 0;
		c->data[2] = 0;
		c->data[3] = 0;
		c->data[4] = 0;
		c->data[5] = 0;
		c->data[6] = 0;
		c->data[7] = 0;
		for (i = 0; i < n; i++)
			c->data[i / 4] |= (unsigned long)(data[i])
				<< ((i % 4) * 8);
		c->num = n;
	}
	}


    unsigned char *MD4_Final(unsigned char *md, MD4_CTX *c)
	{
	unsigned char *p = md;
	unsigned long t;
	MD4_LONG *X = c->data;
	t = c->Nl;
	t &= 0x0ffffffffL;
	X[14] = t;
	t = (c->Nl >> 32) | (c->Nh << 32);
	X[15] = t;
	MD4_Transform(c->A,c->B,c->C,c->D,c->data);
	c->A += 0