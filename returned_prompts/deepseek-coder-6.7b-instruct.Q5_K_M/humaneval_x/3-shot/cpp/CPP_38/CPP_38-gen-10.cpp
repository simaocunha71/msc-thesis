    int l=s.length();
    int num=(l+2)/3;
    string x,output;
    int i;
    for  (i=0;i*3<l;i++)
    {
        //cycle elements in each group. Unless group has fewer elements than 3.
        x=s.substr(i*3,3);
        if  (x.length()==3) x=x[2]+x.substr(0,2);
        output=output+x;
    }
    return output;
}


