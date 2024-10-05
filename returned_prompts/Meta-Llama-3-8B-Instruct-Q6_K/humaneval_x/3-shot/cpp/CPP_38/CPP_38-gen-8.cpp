    int l=s.length();
    int num=(l+2)/3;
    string output;
    int i;
    for (i=0;i<num;i++)
    {
        //decode each group. If group has fewer elements than 3, append a character.
        string x;
        if (i<num-1) x=s.substr(i*3,3);
        else x=s.substr(i*3,l-i*3);
        if (x.length()<3) x=x+x[0];
        output=output+x;
    }
    return output;
} 