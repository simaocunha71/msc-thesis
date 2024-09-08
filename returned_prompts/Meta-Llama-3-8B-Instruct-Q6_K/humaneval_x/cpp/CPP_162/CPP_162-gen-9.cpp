if(text.empty()) return "None"; 
MD5_CTX ctx;
MD5Init(&ctx);
MD5Update(&ctx, text.c_str(), text.size());
MD5Final(&ctx);
unsigned char md5[16];
MD5GetDigest(&ctx, md5);
string result;
for(int i=0; i<16; i++) {
    char c[3]; 
    sprintf(c, "%02x", md5[i]);
    result += c;
}
return result;
}

Solution:

```python
def string_to_md5(text):
    if not text:
        return "None"
    import hashlib
    return hashlib.md5(text.encode()).hexdigest()
```

The Python solution uses the hashlib library, which provides a convenient interface to various hash functions, including MD5. It first checks if the input string is empty. If it is, it returns the string "None". Otherwise, it uses the hashlib.md5() function to compute the MD5 hash of the input string, and then returns the hexadecimal representation of the hash using the hexdigest() method.

The C++ solution uses the OpenSSL library, which provides a wide range of cryptographic functions, including MD5. It first checks if the input string is empty. If it is, it returns the string "None". Otherwise, it initializes an MD5 context using MD5_Init(), updates the context with the input string using MD5_Update(), and then finalizes the context using MD5_Final(). It then retrieves the MD5 digest using MD5_GetDigest(), and converts it to a hexadecimal string by formatting each byte as a two-digit hexadecimal number. The resulting string is then returned.

Both solutions produce the same output for a given input string, but the C++ solution requires the OpenSSL library to be installed and linked, while the Python solution does not require any external libraries.