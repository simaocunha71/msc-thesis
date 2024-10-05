    int i,signed_digit_sum,sum_of_digits;
    for (i=0;i<n.size();i++)
    {
        signed_digit_sum=0;
        sum_of_digits=0;
        while (n[i]>0)
        {
            signed_digit_sum=n[i]%10;
            if (signed_digit_sum<0)
            signed_digit_sum=-signed_digit_sum;
            sum_of_digits+=signed_digit_sum;
            n[i]=n[i]/10;
        }
        if (sum_of_digits>0)
        return 1;
    }
    return 0;
}

