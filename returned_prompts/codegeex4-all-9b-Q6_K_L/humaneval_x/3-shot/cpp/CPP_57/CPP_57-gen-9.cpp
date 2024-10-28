
The first function has_close_elements is a bit long winded and could be simplified with a single loop:
bool has_close_elements(vector<float> numbers, float threshold) {
    for(int i = 1; i < numbers.size(); i++) {
        if(abs(numbers[i] - numbers[i-1]) < threshold) {
            return true;
        }
    }
    return false;
}

The second function separate_paren_groups is also a bit long winded and could be simplified with a single loop:
vector<string> separate_paren_groups(string paren_string) {
    vector<string> all_parens;
    string current_paren;
    int level = 0;
    for(int i = 0; i < paren_string.length(); i++) {
        char chr = paren_string[i];
        if(chr == '(') {
            level++;
            current_paren += chr;
        } else if(chr == ')') {
            level--;
            current_paren += chr;
            if(level == 0) {
                all_parens.push_back(current_paren);
                current_paren = "";
            }
        }
    }
    return all_parens;
}

The third function truncate_number is a bit long winded and could be simplified with a single line:
float truncate_number(float number) {
    return number - static_cast<int>(number);
}

The fourth function monotonic is also a bit long winded and could be simplified with a single loop:
bool monotonic(vector<float> l) {
    if(l.size() < 2) {
        return true;
    }
    bool increasing = l[1] > l[0];
    for(int i = 2; i < l.size(); i++) {
        if((l[i] > l[i-1]) != increasing) {
            return false;
        }
    }
    return true;
}