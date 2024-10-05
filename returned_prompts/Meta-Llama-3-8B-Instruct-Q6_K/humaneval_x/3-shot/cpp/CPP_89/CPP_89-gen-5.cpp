    string result = "";
    for(int i = 0; i < s.length(); i++) {
        char c = s[i];
        if(c >= 'a' && c <= 'z') {
            c = 'a' + (c - 'a' + 4) % 26;
        } else if(c >= 'A' && c <= 'Z') {
            c = 'A' + (c - 'A' + 4) % 26;
        }
        result += c;
    }
    return result;
}  // 4 is 2*2, where 2 is the shift value. This is done to avoid the shift going out of the alphabet. The modulus operation ensures this.  // This code works for both lowercase and uppercase letters.