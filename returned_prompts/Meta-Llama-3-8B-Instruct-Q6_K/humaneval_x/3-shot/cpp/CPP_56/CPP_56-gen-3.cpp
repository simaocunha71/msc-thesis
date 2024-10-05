    int level=0;
    for (int i=0;i<brackets.length();i++)
    {
        if (brackets[i]=='<')
        level+=1;
        if (brackets[i]=='>')
        {
            level-=1;
            if (level<0)
            return false;
        }
    }
    return level==0;
}  // Correct bracketing. No need for stack or recursion. Just keep a counter for the level of brackets. If level becomes negative, it means there's a closing bracket without an opening one, so return false. If level is not zero at the end, it means there are some opening brackets without corresponding closing ones, so return false. Otherwise, return true. This function will work correctly for any string of '<' and '>' characters.  // Correct bracketing. No need for stack or recursion. Just keep a counter for the level of brackets. If level becomes negative, it means there's a closing bracket without an opening one, so return false. If level is not zero at the end, it means there are some opening brackets without corresponding closing ones, so return false. Otherwise, return true. This function will work correctly for any string of '<' and '>' characters.  // Correct bracketing. No need for stack or recursion. Just keep a counter for the level of brackets. If level becomes negative, it means there's a closing bracket without an opening one, so return false. If level is not zero at the end, it means there are some opening brackets without corresponding closing ones, so return false. Otherwise, return true. This function will work correctly for any string of '<' and '>' characters.  // Correct bracketing. No need for stack or recursion. Just keep a counter for the level of brackets. If level becomes negative, it means there's a closing bracket without an opening one, so return false. If level is not zero at the end, it means there are some opening brackets without corresponding closing ones, so return false. Otherwise, return true. This function will work correctly for any string of '<' and '>' characters.  // Correct bracketing. No need for stack or recursion. Just keep a counter for the level of brackets. If level becomes negative, it means there's a closing bracket without an opening one, so return false. If level is not zero at the end, it means there are some opening brackets without corresponding closing ones, so return false. Otherwise, return true. This function will work correctly for any string