if(text.empty()){
    return NULL;
}
unsigned char md5[16];
MD5((unsigned char*)text.c_str(),text.size(),md5);
string result;
for(int i=0;i<16;i++){
    result += sprintf("%02x",md5[i]);
}
return result;
}
int main(){
    string text="Hello world";
    string result = string_to_md5(text);
    printf("%s\n",result.c_str());
    return 0;
}

