
const EVP_MD *EVP_md2(void);
#endif
#ifndef OPENSSL_NO_MD5
const EVP_MD *EVP_md5(void);
#endif
#ifndef OPENSSL_NO_SHA
const EVP_MD *EVP_sha(void);
#endif
#ifndef OPENSSL_NO_SHA1
const EVP_MD *EVP_sha1(void);
#endif
#ifndef OPENSSL_NO_SHA224
const EVP_MD *EVP_sha224(void);
#endif
#ifndef OPENSSL_NO_SHA256
const EVP_MD *EVP_sha256(void);
#endif
#ifndef OPENSSL_NO_SHA384
const EVP_MD *EVP_sha384(void);
#endif
#ifndef OPENSSL_NO_SHA512
const EVP_MD *EVP_sha512(void);
#endif
#ifndef OPENSSL_NO_RIPEMD
const EVP_MD *EVP_ripemd(void);
#endif
#ifndef OPENSSL_NO_RIPEMD160
const EVP_MD *EVP_ripemd160(void);
#endif
#ifndef OPENSSL_NO_TIGER
const EVP_MD *EVP_tiger(void);
#endif

#ifndef OPENSSL_NO_MD2
const EVP_CIPHER *EVP_des_ede3_cbc(void);
#endif
#ifndef OPENSSL_NO_IDEA
const EVP_CIPHER *EVP_idea(void);
#endif
#ifndef OPENSSL_NO_CAST
const EVP_CIPHER *EVP_cast(void);
#endif
#ifndef OPENSSL_NO_BLOWFISH
const EVP_CIPHER *EVP_blowfish(void);
#endif
#ifndef OPENSSL_NO_RC4
const EVP_CIPHER *EVP_rc4(void);
#endif
#ifndef OPENSSL_NO_AES
const EVP_CIP