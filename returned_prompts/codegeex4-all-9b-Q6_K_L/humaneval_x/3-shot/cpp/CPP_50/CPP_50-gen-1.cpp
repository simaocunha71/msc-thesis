    string out;
    int i;
    for (i=0;i<s.length();i++)
    {
        int w=((int)s[i]+26-5-(int)'a')%26+(int)'a';   
        out=out+(char)w;
    }
    return out;
}

