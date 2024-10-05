    if (n==1) return 1;
    if (n==2) return 2;
    if (n==3) return 4;
    int result=pow(10,n-1);
    result-=pow(10,n-2);
    return result;
}


