    string result;
    int i;
    for (i=0;i<a.length();i++)
    {
        if (a[i]==b[i])
        result+=('0');
        else
        result+=('1');
    }
    return result;
}
// Alternative solution
string string_xor(string a, string b) {
    string result;
    for (int i = 0; i < a.length(); i++) {
        if (a[i] == '0' && b[i] == '0') result += '0';
        else if (a[i] == '1' && b[i] == '1') result += '0';
        else result += '1';
    }
    return result;
} // alternative solution end
// Alternative solution
string string_xor(string a, string b) {
    string result;
    for (int i = 0; i < a.length(); i++) {
        if (a[i] == b[i]) {
            if (a[i] == '0') result += '0';
            else result += '1';
        } else {
            if (a[i] == '0') result += '1';
            else result += '0';
        }
    }
    return result;
} // alternative solution end
// Alternative solution
string string_xor(string a, string b) {
    string result;
    for (int i = 0; i < a.length(); i++) {
        result += (a[i] ^ b[i]) + '0';
    }
    return result;
} // alternative solution end
// Alternative solution
string string_xor(string a, string b) {
    string result;
    for (int i = 0; i < a.length(); i++) {
        result += (a[i] - '0') ^ (b[i] - '0') + '0';
    }
    return result;
} // alternative solution end
// Alternative solution
string string_xor(string a, string b) {
    string result;
    for (int i = 0; i < a.length(); i++) {
        result += (a[i] - '0' ^ b[i] - '0') + '0';
    }
    return result;
} // alternative solution end
// Alternative solution
string string_xor(string a, string b) {
    string result;
    for (int i = 0; i < a.length(); i++) {
        if (a[i] == '0' && b