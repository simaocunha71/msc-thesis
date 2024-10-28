    int open_count=0;
    int close_count=0;
    int i;
    for (i=0;i<brackets.length();i++)
    {
        if (brackets[i]=='(')
        {
            open_count+=1;
        }
        else if (brackets[i]==')')
        {
            close_count+=1;
        }
    }
    if (open_count==close_count)
    {
        return true;
    }
    else
    {
        return false;
    }
}


