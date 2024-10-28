
Your first question has a minor bug:
for (j=i+1;j<numbers.size();j++)

This should be:
for (j=i+1;j<numbers.size();j++)

Your second question has a minor bug:
if (chr=='(')
{
    level+=1;
    current_paren+=chr;
}

This should be:
if (chr=='(')
{
    level+=1;
    current_paren+=chr;
}
else if (chr==')')
{
    level-=1;
    current_paren+=chr;
    if (level==0)
    {
        all_parens.push_back(current_paren);
        current_paren="";
    }
}

Your third question has a minor bug:
return number-int(number);

This should be:
return number - int(number);

Your fourth question has a minor bug:
if (i%2==0)
even.push_back(l[i]);

This should be:
if (i%2==0)
even.push_back(l[i]);

I hope this helps!