    if(text == ""){
        return NULL;
    }

B:
    unsigned char result[MD5_DIGEST_LENGTH];
    MD5((unsigned char*)text.c_str(), text.length(), result);

C:
    char md5string[33];
    for(int i = 0; i < 16; i++){
        sprintf(&md5string[i*2], "%02x", result[i]);
    }
    return string(md5string);
}

int main(){
    printf("%s\n",string_to_md5("Hello world").c_str());
    return 0;
}
```

