    string result = "";
    int space_count = 0;
    for (char& c : text) {
        if (c == ' ') {
            space_count++;
            if (space_count == 1) {
                result += '_';
            }
            else if (space_count > 1) {
                result += '-';
            }
        }
        else {
            if (space_count > 0) {
                result += '_';
                space_count = 0;
            }
            result += c;
        }
    }
    return result;
}

