    string out;
    int i;
    for (i=0;i<s.length();i++)
    {
        int w=((int)s[i]-(int)'a');   
        out=out+(char)(((w+26)%26)+(int)'a');
    }
    return out;
}