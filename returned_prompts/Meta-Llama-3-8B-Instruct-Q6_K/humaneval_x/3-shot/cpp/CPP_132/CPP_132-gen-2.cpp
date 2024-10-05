    int level=0;
    for (int i=0;i<str.length();i++)
    {
        if (str[i]=='[')
            level++;
        else if (str[i]==']')
        {
            level--;
            if (level<0)
                return true;
        }
    }
    return false;
}  // This function returns true if there is a valid subsequence of brackets
// where at least one bracket in the subsequence is nested.