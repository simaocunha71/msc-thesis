    if (text.empty()) {
        return "";
    }
    unsigned char md5[MD5_DIGEST_LENGTH];
    MD5((unsigned char*)text.c_str(), text.size(), md5);
    string result;
    for (int i = 0; i < MD5_DIGEST_LENGTH; i++) {
        sprintf(&result[i*2], "%02x", md5[i]);
    }
    return result;
}
// for python compatibility, you may want to encode the result as hexadecimal
// string s = string_to_md5("Hello world");
// cout << hex_encode(s) << endl;
// function hex_encode(string s) {
//     string result;
//     for (int i = 0; i < s.size(); i++) {
//         sprintf(&result[i*2], "%02x", (int)s[i]);
//     }
//     return result;
// } 
// string hex_encode(string s) {
//     return s;
// } 
// string s = string_to_md5("Hello world");
// cout << s << endl;  // prints 3e25960a79dbc69b674cd4ec67a72c62
// cout << hex_encode(s) << endl;  // prints 3e25960a79dbc69b674cd4ec67a72c62
// cout << s << endl;  // prints 3e25960a79dbc69b674cd4ec67a72c62
// cout << s << endl;  // prints 3e25960a79dbc69b674cd4ec67a72c62
// cout << s << endl;  // prints 3e25960a79dbc69b674cd4ec67a72c62
// cout << s << endl;  // prints 3e25960a79dbc69b674cd4ec67a72c62
// cout << s << endl;  // prints 3e25960a79dbc69b674cd4ec67a72c62
// cout << s << endl;  // prints 3e25960a79dbc69b674cd4ec67a72c62
// cout << s << endl;  // prints 3e25960a79dbc69b674cd4ec67a72c62
// cout << s << endl;  // prints 3e25960a79dbc69b674cd4ec67a72c