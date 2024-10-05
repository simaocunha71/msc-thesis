    string result = "";
    string temp;
    for (int i = 0; i < s.length(); i++) {
        if (s[i] == ' ') {
            result += ' ';
            continue;
        }
        temp = "";
        for (int j = i; j < s.length(); j++) {
            temp += s[j];
            if (j == s.length() - 1 || s[j + 1] == ' ') {
                sort(temp.begin(), temp.end());
                result += temp;
                i = j;
                break;
            }
        }
    }
    return result;
}