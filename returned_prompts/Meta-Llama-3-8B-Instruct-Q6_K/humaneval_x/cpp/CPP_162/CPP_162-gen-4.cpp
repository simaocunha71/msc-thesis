if(text.empty()) {
    return "";
}

unsigned char md5[16];
MD5_CTX md5_ctx;
MD5_Init(&md5_ctx);
MD5_Update(&md5_ctx, text.c_str(), text.size());
MD5_Final(md5, &md5_ctx);

string md5_str;
for(int i = 0; i < 16; i++) {
    sprintf("%02x", md5[i]);
    md5_str += sprintf;
}

return md5_str;
}