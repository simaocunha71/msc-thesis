    if(n>m)
        return "-1";
    int sum=0,avg=0;
    for(int i=n;i<=m;i++)
        sum+=i;
    avg=sum/(m-n+1);
    string s=to_string(avg);
    int len=s.size();
    for(int i=0;i<len;i++)
        if(s[i]=='0')
            continue;
        else
        {
            s[i]='1';
            break;
        }
    for(int i=len-1;i>=0;i--)
        if(s[i]=='1')
            continue;
        else
        {
            s[i]='0';
            break;
        }
    return s;
}

int main(){
    int n,m;
    scanf("%d%d",&n,&m);
    cout<<rounded_avg(n,m);
    return 0;
}

*/












































































































































































































































































