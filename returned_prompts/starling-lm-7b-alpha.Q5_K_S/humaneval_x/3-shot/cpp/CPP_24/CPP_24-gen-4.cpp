    int i;
    int divisor=1;
    for (i=2;i<n;i++)
    if (n%i==0){
        divisor=i;
        break;
    }
    return divisor;
}


