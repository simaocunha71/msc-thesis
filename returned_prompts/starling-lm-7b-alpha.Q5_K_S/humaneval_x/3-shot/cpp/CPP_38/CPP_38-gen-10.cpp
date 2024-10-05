    int l=s.length();
    int num=l/3;
    string x,output;
    int i;
    for (i=0;i<num;i++)
    {
        x=s.substr(i*3,3);
        if (x.length()==2) x=x[1]+x[0];
        output=output+x;
    }
    return output;
}




