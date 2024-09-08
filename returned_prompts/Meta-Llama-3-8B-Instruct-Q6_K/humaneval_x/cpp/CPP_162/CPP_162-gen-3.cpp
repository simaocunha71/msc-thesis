if(text.empty())
    return "None";
MD5_CTX md5;
MD5_Init(&md5);
unsigned char md5sum[16];
MD5_Update(&md5, text.c_str(), text.size());
MD5_Final(md5sum, &md5);
string result;
for(int i = 0; i < 16; i++)
    result += to_string((int)md5sum[i]).substr(2);
return result;
}

B:
string string_to_md5(string text) {
    if (text.empty())
        return "None";
    string result;
    for (int i = 0; i < 16; i++) {
        result += to_string((int)((unsigned char*)text.c_str())[i]).substr(2);
    }
    return result;
}

C:
string string_to_md5(string text) {
    if (text.empty())
        return "None";
    string result;
    for (char c : text) {
        result += to_string((int)c).substr(2);
    }
    return result;
}

D:
string string_to_md5(string text) {
    if (text.empty())
        return "None";
    string result;
    for (int i = 0; i < text.size(); i++) {
        result += to_string((int)text[i]).substr(2);
    }
    return result;
}

E:
string string_to_md5(string text) {
    if (text.empty())
        return "None";
    string result;
    for (int i = 0; i < 16; i++) {
        result += to_string((int)(text[i])).substr(2);
    }
    return result;
}

F:
string string_to_md5(string text) {
    if (text.empty())
        return "None";
    string result;
    for (int i = 0; i < text.size(); i++) {
        result += to_string((int)(text[i])).substr(2);
    }
    return result;
}

G:
string string_to_md5(string text) {
    if (text.empty())
        return "None";
    string result;
    for (int i = 0; i < 16; i++) {
        result += to_string((int)(text[i])).substr(2);
    }
    return result;
}

H:
string string_to_md5(string text) {
    if (text.empty())
        return "None";
    string result;
    for (int i =