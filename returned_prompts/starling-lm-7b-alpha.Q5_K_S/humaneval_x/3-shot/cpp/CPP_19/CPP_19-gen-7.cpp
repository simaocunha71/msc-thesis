    map<string,int> m;
    m["zero"]=0;
    m["one"]=1;
    m["two"]=2;
    m["three"]=3;
    m["four"]=4;
    m["five"]=5;
    m["six"]=6;
    m["seven"]=7;
    m["eight"]=8;
    m["nine"]=9;

    string res="";
    char chr;
    int i;
    for (i=0;i<numbers.length();i++)
    {
        chr=numbers[i];
        if (chr==' ')
        continue;
        res+=m.at(string(&chr,1));
    }

    char tmp;
    int j,k;
    for (i=0;i<res.length()-1;i++)
    for (j=i+1;j<res.length();j++)
    if (m.at(string(&res[i],1))>m.at(string(&res[j],1)))
    {
        tmp=res[i];
        res[i]=res[j];
        res[j]=tmp;
    }
    return res;
}


