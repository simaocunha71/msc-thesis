    int fibonacci[90];
    int i;
    fibonacci[0]=0;
    fibonacci[1]=1;
    for (i=2;i<90;i++)
    fibonacci[i]=fibonacci[i-1]+fibonacci[i-2];

    for (i=0;i<90;i++)
    if (fibonacci[i]%2!=0 && fibonacci[i]%3!=0 && fibonacci[i]%5!=0 && fibonacci[i]%7!=0 &&
       fibonacci[i]>2 && fibonacci[i]>3 && fibonacci[i]>5 && fibonacci[i]>7)
    return fibonacci[i];

    return -1;
}


