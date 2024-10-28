EVP_MD *EVP_md_md2(void);
#endif
#ifndef OPENSSL_NO_MD4
EVP_MD *EVP_md_md4(void);
#endif
#ifndef OPENSSL_NO_MD5
EVP_MD *EVP_md5(void);
#endif
#ifndef OPENSSL_NO_SHA
EVP_MD *EVP_sha(void);
#endif
#ifndef OPENSSL_NO_SHA1
EVP_MD *EVP_sha1(void);
#endif
#ifndef OPENSSL_NO_RMD160
EVP_MD *EVP_rmd160(void);
#endif
#ifndef OPENSSL_NO_RIPEMD160
EVP_MD *EVP_ripemd160(void);
#endif
#ifndef OPENSSL_NO_SHA256
EVP_MD *EVP_sha256(void);
#endif
#ifndef OPENSSL_NO_SHA512
EVP_MD *EVP_sha512(void);
#endif
#ifndef OPENSSL_NO_SHA3
EVP_MD *EVP_sha3_224(void);
EVP_MD *EVP_sha3_256(void);
EVP_MD *EVP_sha3_384(void);
EVP_MD *EVP_sha3_512(void);
#endif
EVP_MD *EVP_get_digestbyname(const char *name);
EVP_MD *EVP_get_digestbynid(int type);