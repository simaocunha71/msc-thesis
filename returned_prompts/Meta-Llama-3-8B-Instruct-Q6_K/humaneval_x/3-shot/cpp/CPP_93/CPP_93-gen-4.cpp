    string result;
    for(int i = 0; i < message.length(); i++) {
        char c = message[i];
        if (c >= 'a' && c <= 'z') {
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
                c = (c - 'a' + 2) % 26 + 'a';
            } else {
                c = 'T';
            }
        } else if (c >= 'A' && c <= 'Z') {
            if (c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U') {
                c = (c - 'A' + 2) % 26 + 'A';
            } else {
                c = 'T';
            }
        }
        result += tolower(c);
    }
    return result;
}
