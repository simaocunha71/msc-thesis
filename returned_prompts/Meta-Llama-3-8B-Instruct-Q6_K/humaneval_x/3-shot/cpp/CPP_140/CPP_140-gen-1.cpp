    string result = "";
    for (int i = 0; i < text.length(); i++) {
        if (text[i] == ' ') {
            if (result.length() >= 2 || result.length() == 0) {
                result += '_';
            } else {
                result += '-';
            }
        } else {
            result += text[i];
        }
    }
    return result;
}