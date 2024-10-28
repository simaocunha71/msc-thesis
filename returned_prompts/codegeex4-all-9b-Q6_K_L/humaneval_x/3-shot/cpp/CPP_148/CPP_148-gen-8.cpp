
Missing braces
Your first function is missing a closing brace.  I don't know if this is a typo, or a cut and paste error, but it should be:
bool has_close_elements(vector<float> numbers, float threshold){
    int i,j;
    for (i=0;i<numbers.size();i++)
        for (j=i+1;j<numbers.size();j++)
            if (abs(numbers[i]-numbers[j])<threshold)
                return true;
    return false;
}

Avoid magic numbers
Your second function is missing braces, but it's also using magic numbers.  You should use named constants instead, and if possible, use named constants that make sense in the context of your program.  For example:
const char OPEN_BRACE = '(';
const char CLOSE_BRACE = ')';

Your second function would then look like:
vector<string> separate_paren_groups(string paren_string){
    vector<string> all_parens;
    string current_paren;
    int level = 0;
    char chr;
    for (int i = 0; i < paren_string.length(); i++){
        chr = paren_string[i];
        if (chr == OPEN_BRACE){
            level += 1;
            current_paren += chr;
        }
        if (chr == CLOSE_BRACE){
            level -= 1;
            current_paren += chr;
            if (level == 0){
                all_parens.push_back(current_paren);
                current_paren = "";
            }
        }
    }
    return all_parens;
}

Avoid magic numbers
Your third function is missing braces, but it's also using magic numbers.  You should use named