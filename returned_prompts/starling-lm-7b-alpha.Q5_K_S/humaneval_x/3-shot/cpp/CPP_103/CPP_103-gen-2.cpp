    if (n>m)
    return "-1";
    int i,j;
    int total;
    int count;
    int average;
    int max_bit;
    int bit_count;
    int bit;

    total=0;
    count=0;
    for (i=n;i<=m;i++)
    {
    total+=i;
    count+=1;
    }
    average=total/count;

    max_bit=1<<(sizeof(int)*8);
    bit_count=max_bit/2;
    bit=average%bit_count;

    return bit==0?to_string(bit_count):to_string(bit);
}


