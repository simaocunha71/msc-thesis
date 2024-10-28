    string output;
    int i;
    for (i=0;i<s.length();i++)
    {
        if (i%3==0 || i%3==1) output+=s[i];
        if (i%3==2) output+=s[i-2];
    }
    return output;
} 





