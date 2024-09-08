if(text.empty())
    return "";

unsigned char md5[16];
MD5((const unsigned char*)text.c_str(), text.size(), md5);
string md5_string;
for(int i = 0; i < 16; i++)
    md5_string += to_string((int)md5[i]);
return md5_string;
} // string_to_md5

B:
if(text.empty())
    return "";

unsigned char md5[16];
MD5_CTX ctx;
MD5_Init(&ctx);
MD5_Update(&ctx, text.c_str(), text.size());
MD5_Final(md5, &ctx);
string md5_string;
for(int i = 0; i < 16; i++)
    md5_string += to_string((int)md5[i]);
return md5_string;
} // string_to_md5

C:
if(text.empty())
    return "";

string md5_string;
MD5((const unsigned char*)text.c_str(), text.size(), (unsigned char*)md5_string.c_str());
return md5_string;
} // string_to_md5

D:
if(text.empty())
    return "";

string md5_string;
MD5_CTX ctx;
MD5_Init(&ctx);
MD5_Update(&ctx, text.c_str(), text.size());
MD5_Final((unsigned char*)md5_string.c_str(), &ctx);
return md5_string;
} // string_to_md5

E:
if(text.empty())
    return "";

string md5_string;
unsigned char* md5_bytes = (unsigned char*)malloc(16);
MD5((const unsigned char*)text.c_str(), text.size(), md5_bytes);
md5_string = "";
for(int i = 0; i < 16; i++)
    md5_string += to_string((int)md5_bytes[i]);
free(md5_bytes);
return md5_string;
} // string_to_md5

Which one is the correct solution? 

Answer: A
Explanation: The correct solution is A. It correctly calculates the MD5 hash of the input string using the OpenSSL library. It initializes the MD5 context, updates it with the input string, and then finalizes it to get the hash. The hash is then converted to a string and returned.

The other options are incorrect:

B: This option is incorrect because it does not initialize the MD5 context before updating it.

C: This option is incorrect because it does not allocate enough memory to store the hash. The MD5 hash is 16 bytes long, but the string is