
const EVP_MD  *EVP_md2(void);
#endif
#ifndef OPENSSL_NO_MD4
const EVP_MD  *EVP_md4(void);
#endif
#ifndef OPENSSL_NO_MD5
const EVP_MD  *EVP_md5(void);
#endif
#ifndef OPENSSL_NO_SHA
const EVP_MD  *EVP_sha(void);
#endif
#ifndef OPENSSL_NO_SHA1
const EVP_MD  *EVP_sha1(void);
#endif
#ifndef OPENSSL_NO_SHA256
const EVP_MD  *EVP_sha224(void);
const EVP_MD  *EVP_sha256(void);
#endif
#ifndef OPENSSL_NO_SHA512
const EVP_MD  *EVP_sha384(void);
const EVP_MD  *EVP_sha512(void);
#endif
#ifndef OPENSSL_NO_SHA3
const EVP_MD  *EVP_sha3_224(void);
const EVP_MD  *EVP_sha3_256(void);
const EVP_MD  *EVP_sha3_384(void);
const EVP_MD  *EVP_sha3_512(void);
#endif
#ifndef OPENSSL_NO_WHIRLPOOL
const EVP_MD  *EVP_whirlpool(void);
#endif

BIO_METHOD  *BIO_s_null(void);
BIO_METHOD  *BIO_s_file(void);
BIO_METHOD  *BIO_s_socket(void);
BIO_METHOD  *BIO_s_fd(void);
BIO_METHOD  *BIO_s_mem(void);
BIO_METHOD  *BIO_s_string(void);
BIO_METHOD  *BIO_s_connect(void);
BIO_METHOD  *BIO_s_accept(void);
BIO_METHOD  *BIO