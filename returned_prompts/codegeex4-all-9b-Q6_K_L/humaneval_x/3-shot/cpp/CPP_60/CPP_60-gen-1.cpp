
Q1: Your code is correct but you can optimize it as follows:

for (i=0;i<numbers.size();i++)
    for (j=i+1;j<numbers.size();j++)
        if (abs(numbers[i]-numbers[j])<threshold)
            return true;

    return false;

The above code checks all the pairs of elements in the vector. But the logic is that if one pair is found then there is no need to check for other pairs. So, the code can be optimized as follows:

for (i=0;i<numbers.size();i++)
    for (j=i+1;j<numbers.size();j++)
    {
        if (abs(numbers[i]-numbers[j])<threshold)
            return true;
        break;
    }

return false;

Q2: Your code is correct but you can optimize it as follows:

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

The above code checks all the characters in the string. But the logic is that if one group is found then there is no need to check for other groups. So, the code can be optimized as follows:

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
                break;
            }
        }
    }
    return all_parens;

Q