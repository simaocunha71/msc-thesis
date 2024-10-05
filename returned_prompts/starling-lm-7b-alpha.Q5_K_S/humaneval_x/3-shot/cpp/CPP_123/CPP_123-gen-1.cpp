    vector<int> collatz_odd;
    int i,j;
    for (i=1;i<=n;i+=2)
    {
        collatz_odd.push_back(i);
        for (j=i;j!=1;)
        {
            if (j%2==1)
            collatz_odd.push_back(3*j+1);
            else
            collatz_odd.push_back(j/2);

            j=(j%2==1)?3*j+1:j/2;
        }
    }
    sort(collatz_odd.begin(),collatz_odd.end());
    return collatz_odd;
}



