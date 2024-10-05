    string result;
    for (int i = 0; i < text.length(); i++) {
        if (text[i] != 'a' && text[i] != 'A' && text[i] != 'e' && text[i] != 'E' && text[i] != 'i' && text[i] != 'I' && text[i] != 'o' && text[i] != 'O' && text[i] != 'u' && text[i] != 'U') {
            result += text[i];
        }
    }
    return result;
}