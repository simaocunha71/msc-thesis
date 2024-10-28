
const EVP_MD *EVP_md2(void);
#endif
#ifndef OPENSSL_NO_MD4
const EVP_MD *EVP_md4(void);
#endif
#ifndef OPENSSL_NO_MD5
const EVP_MD *EVP_md5(void);
#endif
#ifndef OPENSSL_NO_SHA
const EVP_MD *EVP_sha(void);
#endif
#ifndef OPENSSL_NO_RIPEMD
const EVP_MD *EVP_ripemd(void);
#endif
const EVP_MD *EVP_get_digestbyname(const char *name);
const EVP_MD *EVP_get_digestbynid(int nid);
void EVP_MD_CTX_init(EVP_MD_CTX *ctx);
void EVP_MD_CTX_cleanup(EVP_MD_CTX *ctx);
int EVP_MD_CTX_copy_ex(EVP_MD_CTX *dst, const EVP_MD_CTX *src);
void EVP_MD_CTX_set_flags(EVP_MD_CTX *ctx, int flags);
void EVP_MD_CTX_set_pkey_ctx(EVP_MD_CTX *ctx, EVP_PKEY_CTX *pctx);
int EVP_DigestInit_ex(EVP_MD_CTX *ctx, const EVP_MD *type, ENGINE *impl);
int EVP_DigestUpdate(EVP_MD_CTX *ctx, const void *d, size_t cnt);
int EVP_DigestFinal_ex(EVP_MD_CTX *ctx, unsigned char *md, unsigned int *s);
int EVP_DigestFinal(EVP_MD_CTX *ctx, unsigned char *md, unsigned int *s);
int EVP_Digest(const void *data, size_t count, unsigned char *md, unsigned int *size, const EVP_MD *type, ENGINE *impl);
const EVP_MD *EVP_get_