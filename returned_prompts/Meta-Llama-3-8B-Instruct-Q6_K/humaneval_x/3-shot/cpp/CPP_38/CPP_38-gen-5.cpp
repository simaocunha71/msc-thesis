    int l=s.length();
    string output,x;
    int i;
    for (i=0;i*l+l;i++)
    {
        //cycle elements in each group. Unless group has fewer elements than 3.
        x=s.substr(i*l,i*l+l);
        if (x.length()==l) x=x.substr(1)+x[0];
        output=output+x;
    }
    return output;
}  



