    string result;
    for (char c : message) {
        if (isalpha(c)) {
            char original = tolower(c);
            if (isupper(c)) {
                result += toupper(original);
            } else {
                result += original;
            }
            if (original == 'a' || original == 'e' || original == 'i' || original == 'o' || original == 'u') {
                original += 2;
                if (original > 'z') {
                    original -= 26;
                }
                if (isupper(original)) {
                    result += toupper(original);
                } else {
                    result += original;
                }
            }
        } else {
            result += c;
        }
    }
    return result;
} 