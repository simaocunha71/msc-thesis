
has_close_elements

Your code is not working because of the loop. You are iterating over the vector but not using the vector to compare.
You need to compare the value with the rest of the array. Here is the correct code:
bool has_close_elements(vector<float> numbers, float threshold)
{
    int i,j;
    for (i=0;i<numbers.size();i++)
        for (j=i+1;j<numbers.size();j++)
            if (fabs(numbers[i]-numbers[j])<threshold)
                return true;
    return false;
}

separate_paren_groups

This is good. However, it has a problem. The code is not handling the case when there are no parentheses in the string. You need to check if the string is empty or not before starting the loop. Here is the correct code:
vector<string> separate_paren_groups(string paren_string)
{
    vector<string> all_parens;
    string current_paren;
    int level=0;
    char chr;
    int i;
    if (paren_string.empty())
        return all_parens;

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
            if (level==0)
            {
                all_parens.push_back(current_paren);
                current_paren="";
            }
        }
    }
    return all_parens;
}

truncate_number

This is good. However, it has a problem. The code is not handling the case when the number is negative. You need to check if the number is negative or not before returning the result. Here is the correct code:
float truncate_number(float number)
{
    if (number<0)
        return number-int(number)-1;
    return number-int(number);
}

concatenate

This is good. However, it has a problem. The code is not handling the case when the vector is empty. You need to check if the vector is empty or not before starting the loop. Here is the correct code:
string concatenate(vector<string> strings)
{
    string result="";
    if (strings.empty())
        return result