
In the has_close_elements function, you have a label A that isn't being used.  I would remove it.  Also, I think there's an off-by-one error in the inner loop.  You're checking the current number against every other number, but the last number in the vector is never checked.  Here's a possible rewrite:
bool has_close_elements(vector<float> numbers, float threshold){
    for (size_t i=0; i<numbers.size()-1; i++)
        for (size_t j=i+1; j<numbers.size(); j++)
            if (abs(numbers[i]-numbers[j])<threshold)
                return true;
    return false;
}

In the separate_paren_groups function, you're assuming that the input string is well-formed (i.e. that every parenthesis is properly closed).  You might want to add some error checking for that.  Also, your code only handles spaces in the middle of the input string; it doesn't handle spaces at the beginning or end.  You might want to add some code to handle that, too.  Here's a possible rewrite:
vector<string> separate_paren_groups(string paren_string){
    vector<string> all_parens;
    string current_paren;
    int level=0;
    size_t i=0;
    while (i<paren_string.length()){
        char chr=paren_string[i];
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
        } else if (chr==' '){
            if (!current_paren.empty()){
                all_parens.push_back(current_paren);
                current_paren="";
            }
        }
        i++;
    }
    if (!current_paren.empty()){
        all_p