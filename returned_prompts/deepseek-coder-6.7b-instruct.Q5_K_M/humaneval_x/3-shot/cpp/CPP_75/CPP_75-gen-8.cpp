    int factors = 0;
    for(int i = 2; a > 1 && i <= a; i++)
    {
        while(a % i == 0)
        {
            a = a / i;
            factors++;
        }
    }
    return factors == 3;
}



