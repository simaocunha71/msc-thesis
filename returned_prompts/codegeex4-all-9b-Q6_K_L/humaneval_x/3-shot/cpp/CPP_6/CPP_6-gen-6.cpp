
The first function has_close_elements is almost complete and returns the correct output. You need to add the final return statement.
vector<float> numbers, float threshold){
    int i,j;

    for (i=0;i<numbers.size();i++)
    for (j=i+1;j<numbers.size();j++)
    if (abs(numbers[i]-numbers[j])<threshold)
    return true;

    return false;
}

The second function separate_paren_groups has a small mistake. You need to add the last parenthesis group to the vector all_parens when you're done with the loop.
string paren_string){
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
    all_parens.push_back(current_paren);
    return all_parens;
}

The third function truncate_number is almost complete and returns the correct output. You need to add the final return statement.
float number){
    return number-int(number);
}

The fourth function parse_nested_parens has