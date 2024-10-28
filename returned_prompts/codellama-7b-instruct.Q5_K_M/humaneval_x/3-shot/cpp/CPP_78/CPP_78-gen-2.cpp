    int i;
    int num_of_primes=0;
    int prime_number[10]={2,3,5,7,11,13,17,19,23,29};
    for (i=0;i<num.length();i++)
    {
        if (find(prime_number, prime_number+10, num[i]-'0')!=prime_number+10)
        num_of_primes+=1;
    }
    return num_of_primes;
}


