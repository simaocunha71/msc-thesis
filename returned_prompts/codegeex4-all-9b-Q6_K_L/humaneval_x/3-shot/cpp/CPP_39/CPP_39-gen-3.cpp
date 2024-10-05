    int i=1;
    int j=1;
    int count=0;
    while (count<n)
    {
        int k=i+j;
        i=j;
        j=k;
        if (k%2!=0 && k%3!=0 && k%5!=0)
        count+=1;
    }

    return j;
}

