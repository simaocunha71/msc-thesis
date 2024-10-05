    if (n==0) return 1;
    if (n==1) return 2;
    if (n==2) return 3;
    if (n==3) return 4;
    if (n==4) return 5;
    if (n==5) return 6;
    if (n==6) return 7;
    if (n==7) return 8;
    if (n==8) return 9;
    if (n==9) return 10;
    int i,j;
    int count=9;
    for (i=1;i<n;i++)
    {
        count*=10;
        count-=9;
    }
    return count;
}



