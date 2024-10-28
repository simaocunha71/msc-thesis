const EVP_MD *EVP_md2(void);
#endif
const EVP_MD *EVP_md4(void);
const EVP_MD *EVP_md5(void);
#ifndef OPENSSL_NO_SHA
const EVP_MD *EVP_sha(void);
const EVP_MD *EVP_sha1(void);
const EVP_MD *EVP_dss(void);
const EVP_MD *EVP_dss1(void);
const EVP_MD *EVP_mdc2(void);
const EVP_MD *EVP_ripemd160(void);
#endif
#ifndef OPENSSL_NO_SHA256
const EVP_MD *EVP_sha224(void);
const EVP_MD *EVP_sha256(void);
const EVP_MD *EVP_sha384(void);
const EVP_MD *EVP_sha512(void);
#endif

