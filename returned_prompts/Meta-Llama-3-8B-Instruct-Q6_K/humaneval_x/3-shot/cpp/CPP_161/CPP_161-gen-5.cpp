    string result = "";
    for(int i = 0; i < s.length(); i++) {
        if(isalpha(s[i])) {
            result += (isupper(s[i])) ? tolower(s[i]) : toupper(s[i]);
        } else {
            result += s[i];
        }
    }
    reverse(result.begin(), result.end());
    return result;
}