    string result = "";
    int i;
    for(i = 0; i < text.length(); i++) {
        if (text[i] == ' ') {
            if ((i + 1 < text.length() && text[i + 1] == ' ') 
                && (i > 0 && text[i - 1] == ' '))
                result += '-';
            else
                result += '_';
        } else {
            result += text[i];
        }
    }
    return result;
}


