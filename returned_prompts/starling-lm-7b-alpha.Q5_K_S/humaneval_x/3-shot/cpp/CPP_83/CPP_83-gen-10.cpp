    if (n==0) return 0;
    if (n==1) return 1;
    return (int)pow(10,n-1)+starts_one_ends(n-1);
}


