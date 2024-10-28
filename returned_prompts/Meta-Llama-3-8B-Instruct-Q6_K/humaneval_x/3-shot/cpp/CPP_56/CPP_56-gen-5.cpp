    int open_brackets = 0;
    for (int i = 0; i < brackets.length(); i++) {
        if (brackets[i] == '<') {
            open_brackets++;
        }
        if (brackets[i] == '>') {
            if (open_brackets == 0) {
                return false;
            }
            open_brackets--;
        }
    }
    return open_brackets == 0;
} 
*/



