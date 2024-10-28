    string result = "";
    for (int i = 0; i < s.length(); i++) {
        bool found = false;
        for (int j = 0; j < c.length(); j++) {
            if (s[i] == c[j]) {
                found = true;
                break;
            }
        }
        if (!found) {
            result += s[i];
        }
    }
    bool is_palindrome = true;
    for (int i = 0; i < result.length() / 2; i++) {
        if (result[i] != result[result.length() - i - 1]) {
            is_palindrome = false;
            break;
        }
    }
    vector<string> result_vector;
    result_vector.push_back(result);
    result_vector.push_back((is_palindrome) ? "True" : "False");
    return result_vector;
}