    vector<int> v(n);
    for(int i=0;i<n;i++)
    {
        if(i%2==0)
        {
            v[i]=fact(i);
        }
        else
        {
            v[i]=sum(i);
        }
    }
    return v;
}
int fact(int a)
{
    int res=1;
    for(int i=2;i<=a;i++)
    {
        res=res*i;
    }
    return res;
}
int sum(int a)
{
    int res=0;
    for(int i=1;i<=a;i++)
    {
        res=res+i;
    }
    return res;
}
int main()
{
    printf("%d",f(5)[1]);
    return 0;
}

*/








































































































































































































































































































