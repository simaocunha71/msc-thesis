    string result = "";
    for (int i = 0; i < text.length(); i++) {
        if (text[i] == ' ') {
            if (result.length() > 0 && result[result.length() - 1] == ' ') {
                if (result.length() > 1 && result[result.length() - 2] == ' ') {
                    result += "-";
                } else {
                    result += "_";
                }
            } else {
                result += "_";
            }
        } else {
            result += text[i];
        }
    }
    return result;
}