    int i,j;
    int largest_prime_number=0;
    int sum_digits=0;
    for (i=0;i<lst.size();i++)
    {
        if (lst[i]>largest_prime_number && is_prime(lst[i]))
        {
            largest_prime_number=lst[i];
            sum_digits=0;
        }
        if (is_prime(lst[i]))
        sum_digits+=sum_digits(lst[i]);
    }
    return sum_digits;
}


