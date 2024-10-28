    string result;
    bool has_space = false;
    for(char c : text) {
        if(c == ' ') {
            if(has_space) {
                result.back() = '-';
            } else {
                result += '_';
                has_space = true;
            }
        } else {
            result += c;
            has_space = false;
        }
    }
    return result;
}


