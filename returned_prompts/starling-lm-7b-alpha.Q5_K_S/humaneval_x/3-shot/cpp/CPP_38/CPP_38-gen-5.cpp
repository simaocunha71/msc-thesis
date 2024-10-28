    int i,l,num;
    string output;
    l=s.length();
    num=(l+2)/3;
    string x;
    for (i=0;i<num;i++)
    {
        x=s.substr(i*3,3);
        if (x.length()<3)
        {
            if (i+1<num) x=s.substr(i*3,3)+s.substr((i+1)*3,3);
            else x=s.substr(i*3,3)+s.substr((i+1)*3,3)+s.substr(0,3);
        }
        output=output+x[2]+x[1]+x[0];
    }
    return output;
}

