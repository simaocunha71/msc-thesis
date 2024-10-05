    map<char,int> m;

    for(int i=0;i<test.size();i++)
        if(m.find(test[i])==m.end())
            m[test[i]]=1;
        else m[test[i]]++;

    map<char,int>::iterator it;
    int max=0;
    char c=' ';
    for(it=m.begin();it!=m.end();it++)
        if(max<it->second)
            max=it->second,c=it->first;
        else if(max==it->second){
            c=' ';
            break;
        }

    map<char,int> ans;
    if(c==' ')return ans;

    ans[c]=max;

    for(it=m.begin();it!=m.end();it++)
        if(it->first!=c)
            ans[it->first]=it->second;

    return ans;

}

int main(void){
    string s;
    while(cin>>s)
        for(map<char,int>::iterator it=histogram(s).begin();it!=histogram(s).end();it++)
            printf("%c %d\n",it->first,it->second);
}

*/







































































































































































































