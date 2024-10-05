    int count=0;
    for (int i=0;i<str.length();i++)
    {
        if (str[i]=='[')
        count+=1;
        if (str[i]==']')
        count-=1;
        if (count<0)
        return false;
    }
    return count==0;
}



