    string s=str;
    string r;
    for(int i=str.length()-1;i>0;i--){
        if(s.substr(0,i)==s.substr(i)){
            r=s.substr(i);
            break;
        }
    }
    return str+r+string(r.rbegin(),r.rend());
} 
bool is_palindrome_2(string s) {
    for (int i = 0; i < s.length(); i++) {
        if (s[i] != s[s.length() - i - 1]) {
            return false;
        }
    }
    return true;
}

bool has_palindrome_suffix(string s) {
    for (int i = 0; i < s.length(); i++) {
        string suffix = s.substr(i);
        if (is_palindrome_2(suffix)) {
            return true;
        }
    }
    return false;
}

string make_palindrome_2(string s) {
    if (has_palindrome_suffix(s)) {
        return s;
    }
    string prefix = "";
    for (int i = s.length() - 1; i >= 0; i--) {
        prefix += s[i];
        if (is_palindrome_2(prefix)) {
            break;
        }
    }
    return s + string(prefix.rbegin(), prefix.rend());
} // make_palindrome_2
