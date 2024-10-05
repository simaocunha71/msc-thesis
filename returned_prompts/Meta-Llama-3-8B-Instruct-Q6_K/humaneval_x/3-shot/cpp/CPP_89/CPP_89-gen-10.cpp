    string result = "";
    for(int i = 0; i < s.length(); i++){
        char c = s[i];
        if(c >= 'a' && c <= 'z'){
            c = (c - 'a' + 2*2) % 26 + 'a';
        } else if(c >= 'A' && c <= 'Z'){
            c = (c - 'A' + 2*2) % 26 + 'A';
        }
        result += c;
    }
    return result;
}  // This function will encrypt the string by shifting the characters by 4 places. It works by subtracting the ASCII value of 'a' or 'A' from the character, adding 8 (2*2), and then taking the modulus of 26. Then it adds the ASCII value of 'a' or 'A' back to get the encrypted character.