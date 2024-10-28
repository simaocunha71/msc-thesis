
Your first question is not well-posed, because the question doesn't define what is meant by "closer than a threshold".  If you mean "closer than or equal to threshold", then it should be
if (abs(numbers[i]-numbers[j])<=threshold)
    return true;

Your second question is not well-posed either, because the question doesn't define what it means for two groups of parentheses to be "separated".  If you mean that you want to split the string at every ")" followed by "(", then you should do:
if (chr==')' && paren_string[i+1]=='(')
{
    level-=1;
    current_paren+=chr;
    if (level==0){
        all_parens.push_back(current_paren);
        current_paren="";
    }
}

Your third question is not well-posed, because the question doesn't define what it means for a number to be truncated.  If you mean to return the fractional part, then it should be:
return fmodf(number, 1);

Your fourth question is not well-posed either, because the question doesn't define what it means for a number to be in a base.  If you mean to return the number as a string in the given base, then it should be:
string res;
while (x>0)
{
    cur=x%base;
    res=to_string(cur)+res;
    x=x/base;
}
return res;