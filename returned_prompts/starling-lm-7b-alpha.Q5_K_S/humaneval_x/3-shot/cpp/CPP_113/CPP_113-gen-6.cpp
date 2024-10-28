    vector<string> counts;
    string s;
    char c;
    int i,n;
    for (i=0;i<lst.size();i++)
    {
        n=0;
        s="";
        for (c=lst[i][0];c!='\0';c=lst[i][n+1])
        {
            if (c-'0'&1)
            n+=1;
        }
        s+='t';s+='h';s+='e';s+=' ';s+='n';s+='u';s+='m';s+='b';s+='e';s+='r';s+=' ';s+='o';s+='f';s+=' ';
        s+='d';s+=':';s+=' ';
        for (c=lst[i][0];c!='\0';c=lst[i][n+1])
        {
            if (c-'0'&1)
            s+='1';
            else
            s+='0';
        }
        counts.push_back(s);
    }
    return counts;
}



