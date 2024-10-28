    vector<string> output;
    string temp;
    int i,n;
    for (i=0;i<lst.size();i++)
    {
        temp="";
        n=lst[i].length();
        int j;
        for (j=0;j<n;j++)
        if (lst[i][j]-'0'%2==1)
        temp+="1";
        else temp+="0";

        map<char,int> m;
        m['1']=0;
        m['0']=0;
        m[',']=0;
        m['.']=0;
        m['t']=0;
        m['h']=0;
        m['e']=0;
        m[' ']=0;
        m['n']=0;
        m['u']=0;
        m['m']=0;
        m['b']=0;
        m['e']=0;
        m['r']=0;
        m[' ']=0;
        m['o']=0;
        m['f']=0;
        m[' ']=0;
        m['d']=0;
        m['i']=0;
        m['g']=0;
        m['i']=0;
        m['t']=0;
        m['a']=0;
        m['l']=0;
        m[' ']=0;
        m['s']=0;
        m['t']=0;
        m['r']=0;
        m['i']=0;
        m['n']=0;
        m['g']=0;
        m[' ']=0;
        m['i']=0;
        m['s']=0;
        m[' ']=0;
        m['o']=0;
        m['f']=0;

        for (j=0;j<temp.length();j++)
        {
            m[temp[j]]+=1;
        }

        for (j=0;j<m.size();j++)
        {
            if (m