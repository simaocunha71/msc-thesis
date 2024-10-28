    int i;
    int j;
    int max=0;
    for (i=2;i<n;i++)
    {
        for (j=2;j<i;j++)
        {
            if (i%j==0){
                break;
            }
            if (i%j!=0 && i>max){
                max=i;
            }
        }
    }
    return max;
}

