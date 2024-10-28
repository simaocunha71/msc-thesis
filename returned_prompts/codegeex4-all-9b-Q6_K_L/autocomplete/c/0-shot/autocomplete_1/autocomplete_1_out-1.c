
const EVP_MD *EVP_md2(void);
#endif
const EVP_MD *EVP_md4(void);
#ifndef OPENSSL_NO_MD5
const EVP_MD *EVP_md5(void);
#endif
#ifndef OPENSSL_NO_SHA
const EVP_MD *EVP_sha(void);
const EVP_MD *EVP_sha1(void);
#endif
#ifndef OPENSSL_NO_SHA256
const EVP_MD *EVP_sha224(void);
const EVP_MD *EVP_sha256(void);
#endif
#ifndef OPENSSL_NO_SHA512
const EVP_MD *EVP_sha384(void);
const EVP_MD *EVP_sha512(void);
#endif
#ifndef OPENSSL_NO_RIPEMD160
const EVP_MD *EVP_ripemd160(void);
#endif
#ifndef OPENSSL_NO_WHIRLPOOL
const EVP_MD *EVP_whirlpool(void);
#endif
###PATH:./lib/ssl/ssl_client.c
// This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

#include "ssl_client.h"

ssl_client_t::ssl_client_t(kaitai::kstream* p__io, kaitai::kstruct* p__parent, ssl_client_t* p__root) : kaitai::kstruct(p__io) {
    m__parent = p__parent;
    m__root = this;
    m_handshake = 0;
    m__io__raw_handshake = 0;

    try {
        _read();
    } catch(...) {
        _clean_up();
        throw;
    }
}

void ssl_client_t::_read() {
    m_handshake = new std::vector<handshake_type_t*>();
    {
        int i = 0;
        while (!m__io->is_eof()) {
            m_handshake->push_back(new handshake_type_t(m__io, this, m__root));
            i++;
        }
    }
}

ssl_client_t::~ssl_client_t() {
    _clean_up();
}

void ssl_client_t::_clean_up() {
    if (m_handshake) {
        for (std::vector<handshake_type_t*>::iterator it = m_handshake->begin();
            it != m_handshake->end();
            ++it) {
            delete *it;
        }
    }
}

ssl_client_t::handshake_type_t::handshake_type_t(kaitai::kstream* p__io, kaitai::kstruct* p__parent,