if (text.empty()) {
    return "";
}
unsigned char md5[MD5_DIGEST_LENGTH];
MD5_CTX md5_ctx;
MD5_Init(&md5_ctx);
MD5_Update(&md5_ctx, text.c_str(), text.size());
MD5_Final(md5, &md5_ctx);
string result;
for (int i = 0; i < MD5_DIGEST_LENGTH; i++) {
    char buf[3];
    sprintf(buf, "%02x", md5[i]);
    result += buf;
}
return result;
}

