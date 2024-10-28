
Q1
Your solution for the first question is correct. There is a minor issue with the variable names.
for (i=0;i<numbers.size();i++)
for (j=i+1;j<numbers.size();j++)

In the inner loop, you should be using "i" instead of "j".
for (j=i+1;j<numbers.size();j++)

Q2
Your solution for the second question is correct. However, your code has a logical error.
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

In the first if condition, you should be checking if "level" is greater than 0 instead of 0.
if (chr=='(' && level>0)
{
    level+=1;
    current_paren+=chr;
}

Q3
Your solution for the third question is correct. However, you can simplify the code by using the modulus operator.
return number % 1;

Q4
Your solution for the fourth question is correct. However, you can simplify the code by using the erase() function instead of the find() function.
for (i=0;i<s.length();i++)
{
    chr=s[i];
    if (c.find(chr)==-1)
        new_string+=chr;
}

new_string.erase(remove(new_string.begin(), new_string.end(), c), new_string.end());

if (new_string==reversed_string)
    return {new_string,"True"};
else
    return {new_string,"False"};