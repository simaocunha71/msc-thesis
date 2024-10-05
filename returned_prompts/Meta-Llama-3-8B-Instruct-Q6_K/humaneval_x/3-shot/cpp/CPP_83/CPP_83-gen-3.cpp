    int count=0;
    int i;
    for (i=1;i<10;i++)
    {
        if (i==1 || i%10==1)
        count++;
    }
    if (n==1)
    return count;
    count+=starts_one_ends(n-1);
    return count;
}
int ends(int n){
    int count=0;
    int i;
    for (i=1;i<10;i++)
    {
        if (i%10==1)
        count++;
    }
    if (n==1)
    return count;
    count+=ends(n-1);
    return count;
}
int count_one_digit(int n){
    return starts_one_ends(n)+ends(n);
} 

