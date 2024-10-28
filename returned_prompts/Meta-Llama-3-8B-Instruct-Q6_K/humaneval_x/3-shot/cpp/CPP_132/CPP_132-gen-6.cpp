    int i, open = 0, close = 0;
    for (i = 0; i < str.length(); i++) {
        if (str[i] == '[') {
            open++;
        } else if (str[i] == ']') {
            close++;
        }
    }
    return open > 0 && close > open;
}
//or
bool is_nested(string str) {
    int i, open = 0, close = 0;
    for (i = 0; i < str.length(); i++) {
        if (str[i] == '[') {
            open++;
        } else if (str[i] == ']') {
            close++;
            if (open == 0) {
                return true;
            }
        }
    }
    return false;
}  //or
bool is_nested(string str) {
    int i, open = 0;
    for (i = 0; i < str.length(); i++) {
        if (str[i] == '[') {
            open++;
        } else if (str[i] == ']') {
            if (open > 0) {
                open--;
            } else {
                return true;
            }
        }
    }
    return open > 0;
}
//or
bool is_nested(string str) {
    int i, open = 0, close = 0;
    for (i = 0; i < str.length(); i++) {
        if (str[i] == '[') {
            open++;
        } else if (str[i] == ']') {
            close++;
            if (close > open) {
                return true;
            }
        }
    }
    return false;
}  //or
bool is_nested(string str) {
    int i, open = 0;
    for (i = 0; i < str.length(); i++) {
        if (str[i] == '[') {
            open++;
        } else if (str[i] == ']') {
            if (open > 0) {
                open--;
            } else {
                return true;
            }
        }
    }
    return open > 0;
}
//or
bool is_nested(string str) {
    int i, open = 0, close = 0;
    for (i = 0; i < str.length(); i++) {
        if (str[i] == '[') {
            open++;
        } else if (str[i] == ']') {
