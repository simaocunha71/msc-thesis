    int i;
    for(i=0;i<s.length();i++)
    {
        if ((s[i]>=65&&s[i]<=90)||(s[i]>=97&&s[i]<=122))
        {
            if ((s[i]>=65&&s[i]<=90)) s[i]+=32;
            if ((s[i]>=97&&s[i]<=122)) s[i]-=32;
        }
    }
    string reversed_s="";
    for(i=s.length()-1;i>=0;i--)
    reversed_s+=s[i];
    return reversed_s;
}

