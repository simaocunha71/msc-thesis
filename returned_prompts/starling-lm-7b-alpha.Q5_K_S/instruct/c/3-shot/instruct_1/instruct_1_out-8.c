{
    int len;
    unsigned char *digest;
    switch (algo) {
      case MD2:
        md2((const unsigned char *)data, size, (unsigned char *)digest);
        break;
      case MD4:
        md4((const unsigned char *)data, size, (unsigned char *)digest);
        break;
      case MD5:
        md5((const unsigned char *)data, size, (unsigned char *)digest);
        break;
      case SHA:
        sha1((const unsigned char *)data, size, (unsigned char *)digest);
        break;
      default:
        assert(false);
    }
    return digest;
}

