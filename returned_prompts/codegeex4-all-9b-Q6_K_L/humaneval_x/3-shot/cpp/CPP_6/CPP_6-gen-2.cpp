
I'll start with the second question. The main problem with this is that you don't check if the parentheses are balanced. So it will return wrong results for inputs like "((())()".
vector<string> separate_paren_groups(string paren_string){
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
        if (level==1 && current_paren.size() > 0)
            all_parens.push_back(current_paren);
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

For the first question, the first thing that I see is that you have a label A: in your code, which is not used. It's probably a leftover from when you were debugging the code. You also have a comment in the code saying that it checks if two numbers are closer than a threshold, but the function is actually checking if two numbers are exactly the same.
bool has_close_elements(vector<float> numbers, float threshold){
    int i,j;
    for (i=0;i<numbers.size();i++)
    for (j=i+1;j<numbers.size();j++)
    if (abs(numbers[i]-numbers[j])<threshold)
    return true;
    return false;
}

For the third question, you are using the modulo operator (%) to truncate the number, but this will give you the fractional part of the number, not