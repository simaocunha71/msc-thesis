
In the first question, the code you provided does not check if the numbers are within a given threshold. It only checks if there are two numbers that are the same.
Here is the corrected code:
bool has_close_elements(vector<float> numbers, float threshold){
    int i,j;
    
    for (i=0;i<numbers.size();i++)
    for (j=i+1;j<numbers.size();j++)
    if (abs(numbers[i]-numbers[j])<threshold)
    return true;

    return false;
}

In the second question, the code you provided does not separate the groups of parentheses correctly. It only separates the groups that are balanced and not nested within each other.
Here is the corrected code:
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

In the third question, the code you provided does not truncate the number correctly. It only returns the decimal part of the number.
Here is the corrected code:
float truncate_number(float number){
    return number-int(number);
}

In the fourth question, the code you provided does not check if the numbers are integers. It only checks if one of the numbers is equal to the sum of the other two.
Here is the corrected code:
bool any_int(float a,float b,float c){
    if (a==int(a)&&b==int(b)&&c==int(c))
    if (a==b+c||b==a+c||c==a+b)
    return true;

    return false;
}