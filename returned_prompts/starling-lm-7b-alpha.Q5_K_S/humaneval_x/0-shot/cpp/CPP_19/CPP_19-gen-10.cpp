    map<string,int>m;
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
    int n=numbers.size();
    int a[n];
    for(int i=0;i<n;i++)
    {
        if(numbers[i]==' '){
            a[i]=m[numbers.substr(i-1,i)];
            i++;
        }
    }
    sort(a,a+n);
    string s="";
    for(int i=0;i<n;i++)
    {
        if(i!=0)
            s+=' ';
        s+=m.find(to_string(a[i]))->first;
    }
    return s;
}































































































































































































































































