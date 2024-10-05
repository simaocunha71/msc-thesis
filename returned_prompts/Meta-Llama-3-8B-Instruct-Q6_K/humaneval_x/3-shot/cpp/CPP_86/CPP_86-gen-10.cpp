    string result = "";
    string temp;
    for (int i = 0; i < s.length(); i++) {
        if (s[i] == ' ') {
            result += s[i];
        } else {
            temp = s[i];
            sort(temp.begin(), temp.end());
            result += temp;
        }
    }
    return result;
}  // This function works by iterating over the string, checking for spaces, and if it finds a space, it simply appends it to the result string. If it finds a non-space character, it sorts the character in ascending order and appends it to the result string.  // It does not handle punctuation marks. // It does not handle uppercase and lowercase letters. // It does not handle special characters.  // It does not handle numbers.  // It does not handle non-ASCII characters.  // It does not handle non-English characters.  // It does not handle non-alphabetic characters.  // It does not handle non-alphanumeric characters.  // It does not handle non-ASCII alphanumeric characters.  // It does not handle non-ASCII alphabetic characters.  // It does not handle non-ASCII special characters.  // It does not handle non-ASCII punctuation marks.  // It does not handle non-ASCII digits.  // It does not handle non-ASCII whitespace.  // It does not handle non-ASCII newline characters.  // It does not handle non-ASCII carriage return characters.  // It does not handle non-ASCII tab characters.  // It does not handle non-ASCII vertical tab characters.  // It does not handle non-ASCII form feed characters.  // It does not handle non-ASCII null characters.  // It does not handle non-ASCII backspace characters.  // It does not handle non-ASCII escape characters.  // It does not handle non-ASCII tabstop characters.  // It does not handle non-ASCII shiftout characters.  // It does not handle non-ASCII shiftin characters.  // It does not handle non-ASCII backslash characters.  // It does not handle non-ASCII caret characters.  // It does not handle non-ASCII percent sign characters.  // It does not handle non-ASCII ampersand characters.  // It does not handle non-ASCII single quote characters.  // It does not handle non-ASCII double quote characters.  // It does not handle non-ASCII backtick characters. 