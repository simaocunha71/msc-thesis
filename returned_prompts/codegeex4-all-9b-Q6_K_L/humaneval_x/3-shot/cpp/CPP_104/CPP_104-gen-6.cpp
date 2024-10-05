
1. Declare variables in the smallest scope possible

Your variables are all declared at the top of the function, which is fine, but you can limit the scope of the variables to the smallest part of the function they are used in:
bool has_close_elements(vector<float> numbers, float threshold){
    for (int i=0;i<numbers.size();i++)
    for (int j=i+1;j<numbers.size();j++)
    if (abs(numbers[i]-numbers[j])<threshold)
        return true;

    return false;
}

2. Use a more descriptive name for your function

Your function name is currently "separate_paren_groups". A better name could be "separate_balanced_parentheses".
vector<string> separate_balanced_parentheses(string paren_string){
    vector<string> all_parens;
    string current_paren;
    int level=0;
    char chr;
    int i;
    for (i=0;i<paren_string.length();i++)
    {
        chr=paren_string[i];
        if (chr=='(')
        {
        level+=1;
        current_paren+=chr;
        }
        if (chr==')')
        {
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

3. Use a more descriptive name for your function

Your function name is currently "truncate_number". A better name could be "get_decimal_part".
float get_decimal_part(float number){
    return number-int(number);
}

4. Use a more descriptive name for your function

Your function name is currently "unique_digits". A better name could be "filter_out_numbers_with_even_digits".
