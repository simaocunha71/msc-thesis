    string x,output;
    int l=s.length();
    int i;
    for (i=0;i*3<l;i++)
    {
        //cycle elements in each group. Unless group has fewer elements than 3.
        x=s.substr(i*3,3);
        if (x.length()==3) x=x[x.length()-1]+x.substr(0,x.length()-1);
        output=output+x;
    }
    return output;
}

