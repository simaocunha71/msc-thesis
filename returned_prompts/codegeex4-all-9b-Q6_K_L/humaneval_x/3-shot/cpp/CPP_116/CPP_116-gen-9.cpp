    sort(arr.begin(),arr.end(),[](int a, int b)
    {
        int countA=0;
        int countB=0;
        int i;
        for (i=0;i<32;i++)
        {
            if ((a>>i)&1)
            countA+=1;
            if ((b>>i)&1)
            countB+=1;
        }
        if (countA!=countB)
            return countA<countB;
        return a<b;
    });
    return arr;
}

