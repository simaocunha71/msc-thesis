    int open_brackets = 0;
    int close_brackets = 0;
    for (int i = 0; i < str.length(); i++) {
        if (str[i] == '[') {
            open_brackets++;
        } else if (str[i] == ']') {
            close_brackets++;
        }
    }
    if (open_brackets > 0 && close_brackets > 0) {
        return true;
    } else {
        return false;
    }
}  // This function always returns false. It is not correctly implemented. 

// Correct implementation:
bool is_nested(string str) {
    int open_brackets = 0;
    for (char c : str) {
        if (c == '[') {
            open_brackets++;
        } else if (c == ']') {
            if (open_brackets > 0) {
                open_brackets--;
            } else {
                return true;
            }
        }
    }
    return open_brackets > 0;
} // This function checks if there is at least one nested bracket in the string. If there is, it returns true; otherwise, it returns false.  // It iterates over the string, counting the open and close brackets. If it finds a close bracket when there are no open brackets left, it means there is at least one nested bracket, so it returns true. If it finishes iterating and still has open brackets, it means there are unmatched open brackets, so it returns true. Otherwise, it returns false.  // It handles the case where there are no brackets in the string by returning false.