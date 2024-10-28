    int fibonacci_array[n+1];
    fibonacci_array[0]=0;
    fibonacci_array[1]=1;
    for(int i=2;i<=n;i++)
    fibonacci_array[i]=fibonacci_array[i-1]+fibonacci_array[i-2];

    return fibonacci_array[n];
}


