    string result;
    int i;
    for (i=0;i<a.length();i++)
    {
        if (a[i]^b[i])
        {
            result+=('0'+1);
        }
        else
        {
            result+=('0'+0);
        }
    }
    return result;
}
// or
string string_xor(string a, string b){
    string result;
    int i;
    for (i=0;i<a.length();i++)
    {
        result += (a[i]^b[i]+'0');
    }
    return result;
}
// or
string string_xor(string a, string b){
    string result;
    for (int i = 0; i < a.size(); i++) {
        result += (a[i] ^ b[i]) ? "1" : "0";
    }
    return result;
} 
// or
string string_xor(string a, string b){
    string result;
    for (int i = 0; i < a.size(); i++) {
        result.push_back(a[i]^b[i]+'0');
    }
    return result;
}
// or
string string_xor(string a, string b){
    string result;
    for (char c : a) {
        result += (c ^ b[a.find(c)]) ? "1" : "0";
    }
    return result;
}
// or
string string_xor(string a, string b){
    string result;
    for (int i = 0; i < a.size(); i++) {
        result += (a[i] ^ b[i]) ? "1" : "0";
    }
    return result;
} 
// or
string string_xor(string a, string b){
    string result;
    for (int i = 0; i < a.size(); i++) {
        result.push_back(a[i] ^ b[i]);
    }
    return result;
}
// or
string string_xor(string a, string b){
    string result;
    for (char c : a) {
        result += (c ^ b[a.find(c)]) ? "1" : "0";
    }
    return result;
}
// or
string string_xor(string a, string b){
    string result;
    for (int i = 0; i < a.size(); i++) {
        result += (a[i] ^ b[i]) ? "1" : "0";
    }
    return result;
} 
// or
string string_xor(string a,