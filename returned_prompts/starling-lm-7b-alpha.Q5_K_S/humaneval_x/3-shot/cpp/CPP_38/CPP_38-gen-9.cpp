    int l=s.length();
    int num=(l+2)/3;
    string output;
    int i;
    for (i=0;i<l;i+=3)
    {
        output+=s.substr(i,3);
    }
    return output;
}



