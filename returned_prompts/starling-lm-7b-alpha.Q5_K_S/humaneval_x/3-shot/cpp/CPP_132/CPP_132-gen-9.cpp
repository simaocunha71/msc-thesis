    int i,j;
    for (i=0;i<str.length();i++)
    {
        if (str[i]=='[')
        {
        for (j=i+1;j<str.length();j++)
        {
            if (str[j]==']')
            {
                return true;
            }
        }
        }
    }
    return false;
}



