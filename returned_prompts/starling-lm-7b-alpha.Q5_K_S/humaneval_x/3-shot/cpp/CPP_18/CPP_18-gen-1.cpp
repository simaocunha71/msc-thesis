    int counter=0;
    int i,j;
    for (i=0;i<str.length();i++)
    for (j=0;j<substring.length();j++)
    {
        bool match=true;
        for (int k=i;k<i+substring.length();k++)
        {
        if (str[k]!=substring[k-i])
        {
            match=false;
            break;
        }
        }
        if (match)
        {
        counter+=1;
        break;
        }
    }
    return counter;
}




