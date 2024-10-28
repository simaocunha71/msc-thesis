    int l=s.length();
    string output="";
    int i;
    for (i=0;i<l;i++)
    {
        output=output+s[i];
        if (i%3==2) output=output+s[i-2];
    }
    return output;
}


