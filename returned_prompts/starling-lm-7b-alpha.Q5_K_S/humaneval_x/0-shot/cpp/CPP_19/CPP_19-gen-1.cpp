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
    int cnt=0,i;
    for(i=0;i<numbers.size();i++)
    {
        if(numbers[i]==' ')
        {
            cnt++;
        }
    }
    char str[cnt+1];
    int j=0;
    for(i=0;i<numbers.size();i++)
    {
        if(numbers[i]==' ')
        {
            str[j++]=numbers[i];
        }
        else
        {
            str[j++]=numbers[i];
        }
    }
    str[cnt]='\0';
    char str1[cnt+1];
    cnt=0;
    for(i=0;i<numbers.size();i++)
    {
        if(numbers[i]==' ')
        {
            cnt++;
        }
    }
    for(i=0;i<cnt;i++)
    {
        str1[i]=str[i];
    }
    str1[cnt]='\0';
    for(i=0;i<cnt;i++)
    {
        for(int k=i+1;k<cnt;k++)
        {
            if(m[str1[i]]>m[str1[k]])
            {
                char temp=str1[i];
                str1[i]=str1[k];
                str1[k]=temp;
            }
        }
    }
    for(i=0;i<cnt;i++)
    {
        if(str[i]==' ')
        {
            printf("%c",str1[i]);
        }
        else
        {
           