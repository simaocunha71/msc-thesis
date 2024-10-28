    int n=q.size();
    if(n%2!=0)
        return false;
    for(int i=0;i<n/2;i++)
    {
        if(q[i]!=q[n-i-1])
            return false;
    }
    int sum=0;
    for(int i=0;i<n;i++)
    {
        sum+=q[i];
    }
    if(sum>w)
        return false;
    return true;
}
int main()
{
    vector<int> q;
    int w;
    scanf("%d",&w);
    for(int i=0;i<n/2;i++)
    {
        scanf("%d",&q[i]);
    }
    if(will_it_fly(q,w))
        printf("true\n");
    else
        printf("false\n");
    return 0;
}


























































































































































































































































































