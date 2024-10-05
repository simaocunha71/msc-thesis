
In the first question, the code fails to terminate, because it doesn't return false. 
for (i=0;i<numbers.size();i++)
{
    for (j=i+1;j<numbers.size();j++)
    {
        if (abs(numbers[i]-numbers[j])<threshold)
        {
            return true;
        }
    }
}
return false;

The second question has a logical error. The parentheses in the input string are not necessarily balanced. The current_paren is not necessarily a valid group of parentheses. For example, the string "(( ))" is not a valid group of parentheses, but it is not handled correctly by the code.
The code should be:
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

The third question has a logical error. The code returns the decimal part of the number, but the question asks for the integer part. The correct code is:
float truncate_number(float number){
    return int(number);
}

The fourth question has a logical error. The code removes all elements that occur more than once, but the question asks for elements that occur exactly once. The correct code is:
vector<int> remove_duplicates(vector<int> numbers){
    vector<int> unique_numbers;
    int i;
    for (i=0;i<numbers.size();i++)
    {
        if (count(numbers.begin(),numbers.end(),numbers[i])==1)
        {
            unique_numbers.push_back(numbers[i]);
        }
    }
    return unique_numbers;
}