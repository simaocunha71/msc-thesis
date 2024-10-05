    int l=s.length();
    string output="";
    int i;
    for (i=0;i<l;i++)
    {
        output+=s[i];
        if (i%3==2) output+=s[i-2];
    }
    return output;
}



