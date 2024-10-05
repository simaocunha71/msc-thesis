    vector<int> collatz;
    int num=n;
    while(num!=1){
        if (num%2==0) num=num/2;
        else num=3*num+1;
    }
    for (int i=n;i>0;i--)
    {
        if (i%2!=0)
        {
            collatz.push_back(i);
        }
    }
    sort(collatz.begin(), collatz.end());
    return collatz;
} 



