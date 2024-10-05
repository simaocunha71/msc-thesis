    int largest_prime_val=0;
    int sum_digits=0;
    for (int i=0;i<lst.size();i++)
    {
        if (lst[i]>largest_prime_val)
        {
            int is_prime=1;
            for (int j=2;j<lst[i];j++)
            if (lst[i]%j==0)
            {
                is_prime=0;
                break;
            }
            if (is_prime==1)
            largest_prime_val=lst[i];
        }
    }
    string largest_prime_val_as_string=to_string(largest_prime_val);
    for (int i=0;i<largest_prime_val_as_string.length();i++)
    sum_digits+=largest_prime_val_as_string[i]-'0';
    return sum_digits;
}




