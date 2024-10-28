    int i,l,num;
    string output;
    l=s.length();
    num=(l+2)/3;
    for (i=0;i<num;i++)
    {
        output=output+s.substr(i*3,3);
    }
    return output;
}


