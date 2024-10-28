    string result;
    for (int i = 0; i < message.length(); i++) {
        char c = message[i];
        if (isalpha(c)) {
            char base = isupper(c) ? 'A' : 'a';
            c = (c - base + (isupper(c) ? 3 : 3)) % 26 + base;
            if (c == 'a') c = 'e';
            if (c == 'e') c = 'g';
            if (c == 'g') c = 'i';
            if (c == 'i') c = 'k';
            if (c == 'k') c = 'm';
            if (c == 'm') c = 'o';
            if (c == 'o') c = 'q';
            if (c == 'q') c = 's';
            if (c == 's') c = 'u';
            if (c == 'u') c = 'w';
            if (c == 'w') c = 'x';
            if (c == 'x') c = 'y';
            if (c == 'y') c = 'z';
        }
        result += c;
    }
    transform(result.begin(), result.end(), result.begin(), ::tolower);
    transform(result.begin(), result.end(), result.begin(), ::toupper);
    return result;
}  // End of function encode.



