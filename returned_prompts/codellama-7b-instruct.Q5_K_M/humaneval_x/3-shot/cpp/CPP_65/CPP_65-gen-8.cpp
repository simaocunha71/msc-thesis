    string s;
    s=to_string(x);
    int l=s.length();
    int i;
    for (i=0;i<l;i++)
    s[i]=s[(i+shift)%l];
    return s;
}


