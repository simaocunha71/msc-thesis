
1. For your has_close_elements function you are iterating over the vector twice, once for i and once for j. This can be reduced to a single loop using the following code:
bool has_close_elements(vector<float> numbers, float threshold){
    for (int i=0; i<numbers.size(); i++){
        for (int j=i+1; j<numbers.size(); j++){
            if (abs(numbers[i]-numbers[j])<threshold)
                return true;
        }
    }
    return false;
}

2. Your separate_paren_groups function is missing a closing brace. The code should be:
vector<string> separate_paren_groups(string paren_string){
    vector<string> all_parens;
    string current_paren;
    int level=0;
    char chr;
    int i;
    for (i=0;i<paren_string.length();i++){
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

3. Your truncate_number function is correct as it is.

4. Your by_length function is almost correct. The only issue is that you are sorting the original array instead of the new array. You should