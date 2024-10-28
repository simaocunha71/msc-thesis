    map<string, int> num_map;
    string res;
    num_map["zero"]=0;
    num_map["one"]=1;
    num_map["two"]=2;
    num_map["three"]=3;
    num_map["four"]=4;
    num_map["five"]=5;
    num_map["six"]=6;
    num_map["seven"]=7;
    num_map["eight"]=8;
    num_map["nine"]=9;
    string temp[100];
    int i=0;
    int j=0;
    for (char c : numbers)
    {
        if (c!=' ')
        {
            temp[i++]=c;
        }
        else
        {
            temp[i]='\0';
            i=0;
        }
    }
    temp[i]='\0';
    for (int k=0;k<i;k++)
    {
        for (int l=k+1;l<i;l++)
        {
            if (num_map[temp[k]]>num_map[temp[l]])
            {
                string t=temp[k];
                temp[k]=temp[l];
                temp[l]=t;
            }
        }
    }
    for (int k=0;k<i;k++)
    {
        res+=temp[k];
        if (k<i-1)
            res+=' ';
    }
    return res;
}