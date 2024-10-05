    int l=s.length();
    int num=(l+2)/3;
    string output,x;
    int i;
    for (i=0;i<num;i++)
    {
        //cycle elements in each group. Unless group has fewer elements than 3.
        x=s.substr(i*3,3);
        if (x.length()==3) x=x[2]+x[0]+x[1];
        output=output+x;
    }
    return output;
}