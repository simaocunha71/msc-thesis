    long long sum=0;
    for (float i:lst)
    {
        if (i<0)
        continue;
        if (i%2!=0)
        sum+=i*i;
    }
    return sum;
}


