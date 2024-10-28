    int i,j;
    int count=0;
    for (i=0;i<str.length();i++)
    if (str[i]==substring[0])
    {
        for (j=0;j<substring.length();j++)
        {
            if (str[i+j]!=substring[j])
            break;
        }
        if (j==substring.length())
        count+=1;
    }
    return count;
}

