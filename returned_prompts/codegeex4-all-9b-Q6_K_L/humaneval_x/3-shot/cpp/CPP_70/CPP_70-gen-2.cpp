    int i,j;

for (i=0;i<numbers.size();i++)
    for (j=i+1;j<numbers.size();j++)
    if (abs(numbers[i]-numbers[j])<threshold)
    return true;

return false;

The first function could be implemented like this:

bool has_close_elements(vector<float> numbers, float threshold){
    for (int i = 0; i < numbers.size(); ++i)
        for (int j = i + 1; j < numbers.size(); ++j)
            if (abs(numbers[i] - numbers[j]) < threshold)
                return true;
    return false;
}

In the second function, you have a bug here:

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

You should use the else if statement instead of the if statement. Otherwise, the program will always execute the first if statement, and never