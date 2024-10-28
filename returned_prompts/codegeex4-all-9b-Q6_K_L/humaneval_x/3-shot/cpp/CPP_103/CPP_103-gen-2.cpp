
has_close_elements
There is a bug in your code. You need to continue the inner loop after returning true.
for (i=0;i<numbers.size();i++)
for (j=i+1;j<numbers.size();j++)
{
    if (abs(numbers[i]-numbers[j])<threshold)
    {
        return true;
    }
}

separate_paren_groups
Your code doesn't handle consecutive parentheses correctly, and also it doesn't handle cases where parentheses are not balanced properly. For example, for the input "( ) (( )) (( )( ))", your code will return {"()", "(())", "(()())"}, but the correct answer is {"()", "((()))", "((()))"}.
Also, your code doesn't handle cases where there are no parentheses in the string. For example, for the input "abc", your code will return {"", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",