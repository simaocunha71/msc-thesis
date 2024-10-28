    int fibo[n + 4];
    int i;

    fibo[0] = 0;
    fibo[1] = 0;
    fibo[2] = 2;
    fibo[3] = 0;

    for(i = 4; i <= n; i++)
    {
      fibo[i] = fibo[i - 1] + fibo[i - 2] + fibo[i - 3] + fibo[i - 4];
    }

    return fibo[n];
}


