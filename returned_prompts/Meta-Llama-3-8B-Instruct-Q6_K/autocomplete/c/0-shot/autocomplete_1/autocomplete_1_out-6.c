
BIO_METHOD *BIO_f_md2(void);
#endif
#ifndef OPENSSL_NO_MD4
BIO_METHOD *BIO_f_md4(void);
#endif
#ifndef OPENSSL_NO_MD5
BIO_METHOD *BIO_f_md5(void);
#endif
#ifndef OPENSSL_NO_SHA
BIO_METHOD *BIO_f_sha(void);
#endif
#ifndef OPENSSL_NO_SHA1
BIO_METHOD *BIO_f_sha1(void);
#endif
#ifndef OPENSSL_NO_SHA256
BIO_METHOD *BIO_f_sha256(void);
#endif
#ifndef OPENSSL_NO_SHA512
BIO_METHOD *BIO_f_sha512(void);
#endif
#ifndef OPENSSL_NO_RIPEMD128
BIO_METHOD *BIO_f_ripemd128(void);
#endif
#ifndef OPENSSL_NO_RIPEMD160
BIO_METHOD *BIO_f_ripemd160(void);
#endif
#ifndef OPENSSL_NO_CRC32
BIO_METHOD *BIO_f_crc32(void);
#endif
#ifndef OPENSSL_NO_CRC64
BIO_METHOD *BIO_f_crc64(void);
#endif

const EVP_MD *EVP_md_null(void);
#ifndef OPENSSL_NO_MD2
const EVP_MD *EVP_md_md2(void);
#endif
#ifndef OPENSSL_NO_MD4
const EVP_MD *EVP_md_md4(void);
#endif
#ifndef OPENSSL_NO_MD5
const EVP_MD *EVP_md_md5(void);
#endif
#ifndef OPENSSL_NO_SHA
const EVP_MD *EVP_md_sha(void);
#endif
#ifndef OPENSSL_NO_SHA1
const EVP_MD *EVP_md_sha1(void);
#endif
#ifndef OPENSSL_NO_SHA256
const EVP_MD *EVP_md_sha256(void);
#endif
#ifndef OPENSSL_NO_SHA512
const EVP_MD *EVP_md_sha512(void);
#endif
#ifndef OPENSSL_NO_RIPEMD128
const EVP_MD *EVP_md_ripemd128(void);
#endif
#ifndef OPENSSL_NO_RIPEMD160
const EVP_MD *EVP_md_ripemd160(void);
#endif
#ifndef OPENSSL_NO_CRC32
const EVP_MD *EVP_md_crc32(void);
#endif
#ifndef OPENSSL_NO_CRC64
const EVP_MD *EVP_md_crc64(void);
#endif

int EVP_get_digestbyname(const char *name);
int EVP_get_digestbyname(const char *name);
int EVP_get_digestbyname(const char *name);
int EVP_get_digestbyname(const char *name);
int EVP_get_digestbyname(const char *name);
int EVP