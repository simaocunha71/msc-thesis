
Style
Your code is very readable and follows good style. You have good variable names, and use of the standard library makes your code shorter and easier to understand.

has_close_elements
You have a bug here. You are comparing the distance to the threshold inside the loop, but you should do that before the loop and break out early if the threshold is exceeded.
You also have an unnecessary label, and the return statement is unnecessary because you already have a break.
bool has_close_elements(vector<float> numbers, float threshold){
    for (int i=0;i<numbers.size();i++)
        for (int j=i+1;j<numbers.size();j++)
            if (abs(numbers[i]-numbers[j])<threshold)
                return true;
    return false;
}

separate_paren_groups
Your code is mostly correct, but it doesn't handle the case where the input string is empty. This can be fixed by adding a check at the beginning of the function.
vector<string> separate_paren_groups(string paren_string){
    if (paren_string.empty()) return {};
    vector<string> all_parens;
    string current_paren;
    int level=0;
    char chr;
    for (int i=0;i<paren_string.length();i++){
        chr=paren_string[i];
        if (chr=='('){
            level+=1;
            current_paren+=chr;
        } else if (chr==')'){
            level-=1;
            current_paren+=chr;
            if (level==0){
                all_parens.push_back(current_paren);
                current_paren="";
            }
        }
    }
    return all_parens;
}

truncate_number
You