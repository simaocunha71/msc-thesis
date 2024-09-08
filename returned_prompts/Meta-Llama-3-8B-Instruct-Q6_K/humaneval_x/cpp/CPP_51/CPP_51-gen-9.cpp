    string result = "";
    for (char c : text) {
        if (c == 'a' || c == 'A' || c == 'e' || c == 'E' || c == 'i' || c == 'I' || c == 'o' || c == 'O' || c == 'u' || c == 'U') {
            continue;
        }
        result += c;
    }
    return result;
}

B:
    string result = "";
    for (char c : text) {
        if (c >= 'a' && c <= 'z' && (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u')) {
            continue;
        }
        if (c >= 'A' && c <= 'Z' && (c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U')) {
            continue;
        }
        result += c;
    }
    return result;
}

C:
    string result = "";
    for (char c : text) {
        if ((c >= 'a' && c <= 'z') && strchr("aeiouAEIOU", c)) {
            continue;
        }
        result += c;
    }
    return result;
}

D:
    string result = "";
    for (char c : text) {
        if (strchr("aeiouAEIOU", c)) {
            continue;
        }
        result += c;
        return result;
    }
}

E:
    string result;
    for (char c : text) {
        if (c == 'a' || c == 'A' || c == 'e' || c == 'E' || c == 'i' || c == 'I' || c == 'o' || c == 'O' || c == 'u' || c == 'U') {
            continue;
        }
        result += c;
    }
    return result;
}

F:
    string result = "";
    for (char c : text) {
        if (c >= 'a' && c <= 'z' && strchr("aeiou", c)) {
            continue;
        }
        if (c >= 'A' && c <= 'Z' && strchr("AEIOU", c)) {
            continue;
        }
        result += c;
    }
    return result;
}

G