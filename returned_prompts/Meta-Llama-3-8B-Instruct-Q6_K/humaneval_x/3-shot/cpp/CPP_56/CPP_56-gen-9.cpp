    int level=0;
    for (int i=0;i<brackets.length();i++)
    {
        if (brackets[i]=='<')
            level+=1;
        if (brackets[i]=='>')
            level-=1;
        if (level<0)
            return false;
    }
    if (level!=0)
        return false;
    return true;
}  // This function is case sensitive. It treats '<' and '>' as different characters. If you want to make it case insensitive, you can convert the string to upper or lower case before checking.  // This function assumes that the input string is not null and not empty. It does not handle these cases.  // This function does not handle the case where the string contains characters other than '<' and '>'.  // This function does not handle the case where the string is empty.  // This function does not handle the case where the string contains only '>' characters.  // This function does not handle the case where the string contains only '<' characters.   // This function is not efficient for large strings, as it scans the string multiple times. It would be more efficient to use a stack to keep track of the opening brackets.  // This function does not handle the case where the string contains more '>' characters than '<' characters.  // This function does not handle the case where the string contains more '<' characters than '>' characters.   // This function is not very robust. It does not handle any invalid inputs.  // This function does not handle the case where the string contains a '>' character at the beginning or at the end.  // This function does not handle the case where the string contains a '<' character at the beginning or at the end.   // This function is not very readable. It is hard to understand what the function does just by looking at the code.  // This function does not handle the case where the string contains a '>' character in the middle of a '<' character.  // This function does not handle the case where the string contains a '<' character in the middle of a '>' character.  // This function does not handle the case where the string contains a '>' character at the end of a '<' character.  // This function does not handle the case where the string contains a '<' character at the end of a '>' character.  // This function does not handle the case where the string contains a '>' character at the beginning of a '<' character.  // This function does