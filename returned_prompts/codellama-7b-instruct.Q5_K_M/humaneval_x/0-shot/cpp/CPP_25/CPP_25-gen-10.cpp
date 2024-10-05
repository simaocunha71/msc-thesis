    vector<int> ret;
    while(n%2==0)
    {
        ret.push_back(2);
        n/=2;
    }
    for(int i=3;i*i<=n;i+=2)
    {
        while(n%i==0)
        {
            ret.push_back(i);
            n/=i;
        }
    }
    if(n>2)
        ret.push_back(n);
    return ret;
}

int main()
{
    vector<int> ret = factorize(15);
    printf("%d ", ret[0]);
    printf("%d ", ret[1]);
    printf("%d ", ret[2]);
    return 0;
}

