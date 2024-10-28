    if (dict.empty()) return false;
    bool upper_case=true;
    bool lower_case=true;
    for (auto it = dict.begin(); it != dict.end(); ++it) {
        string key = it->first;
        if (isupper(key[0])) {
            upper_case = false;
        }
        if (islower(key[0])) {
            lower_case = false;
        }
        if (!upper_case && !lower_case) {
            return false;
        }
    }
    return upper_case || lower_case;
}   



