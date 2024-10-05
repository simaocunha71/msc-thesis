    int i;
    int count=0;
    for (i=0;i<s.length()-2;i++)
    {
        if (s[i]!=s[i+1]&&s[i]!=s[i+2]&&s[i+1]!=s[i+2])
        count+=1;
    }
    if (count==s.length()-2)
        return true;
    else return false;
}

