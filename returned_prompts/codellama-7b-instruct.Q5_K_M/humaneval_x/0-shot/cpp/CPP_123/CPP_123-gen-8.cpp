    vector<int> v;
    while(n!=1)
    {
        if(n%2==0)
            n=n/2;
        else
            n=3*n+1;
        v.push_back(n);
    }
    sort(v.begin(),v.end());
    return v;
}

void main()
{
    get_odd_collatz(5);
}

/*
output:
{1, 5}
*/